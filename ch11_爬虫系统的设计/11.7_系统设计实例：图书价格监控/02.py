# 对应：第11章 爬虫系统的设计
# 小节：11.7 系统设计实例：图书价格监控
# 条目：11.7.3 完整主程序
# 清单：02
# 说明：摘自书稿示例，未改写。

"""Single scheduler, configurable listing pages; dry-run alerts by default."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from os import getenv
from urllib.parse import urljoin
from uuid import uuid4
import pymysql
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
import traceback
from alerter import Alerter, alert_if_needed
from metrics import SpiderMetrics

SCHEMA = """CREATE TABLE IF NOT EXISTS price_snapshots (
  run_id CHAR(32) NOT NULL,
  url VARCHAR(512) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  title VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  captured_at DATETIME(6) NOT NULL,
  PRIMARY KEY (run_id, url),
  INDEX history (url, captured_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""


def parse(html, url):
    books = []
    for card in BeautifulSoup(html, "html.parser").select("article.product_pod"):
        link, price = card.select_one("h3 a"), card.select_one(".price_color")
        if link is None or price is None or not link.get("href") or not link.get("title"):
            raise ValueError("书籍字段缺失")
        amount = Decimal(price.get_text(strip=True).removeprefix("£"))
        if not amount.is_finite() or amount <= 0:
            raise ValueError("价格必须为正数")
        books.append(dict(url=urljoin(url, link["href"]), title=link["title"], price=amount))
    if not books:
        raise ValueError("列表为空")
    return books


def fetch(url):
    response = requests.get(url, timeout=(5, 15))
    response.raise_for_status()
    response.encoding = "utf-8"
    return parse(response.text, url)


def price_change(old, new, threshold):
    if old is None or old <= 0:
        return None
    change = (new - old) / old
    return change if change != 0 and abs(change) >= threshold else None


class Store:
    def __init__(self, connection):
        self.db = connection
        with self.db.cursor() as cursor:
            cursor.execute(SCHEMA)
        self.db.commit()

    def save(self, run_id, books, threshold):
        captured = datetime.now(timezone.utc).replace(tzinfo=None)
        changes = []
        try:
            with self.db.cursor() as cursor:
                for book in books:
                    cursor.execute("SELECT price FROM price_snapshots WHERE url=%s AND run_id<>%s "
                                   "ORDER BY captured_at DESC LIMIT 1", (book["url"], run_id))
                    row = cursor.fetchone()
                    delta = price_change(row[0] if row else None, book["price"], threshold)
                    cursor.execute("INSERT IGNORE INTO price_snapshots "
                                   "(run_id,url,title,price,captured_at) VALUES (%s,%s,%s,%s,%s)",
                                   (run_id, book["url"], book["title"], book["price"], captured))
                    if cursor.rowcount == 1 and delta is not None:
                        changes.append((book, delta))
                cursor.execute("DELETE FROM price_snapshots WHERE captured_at < %s", (captured - timedelta(days=90),))
            self.db.commit()
            return changes
        except Exception:
            self.db.rollback()
            raise


def connect():
    return pymysql.connect(host=getenv("MYSQL_HOST", "localhost"),
                           port=int(getenv("MYSQL_PORT", "3306")),
                           user=getenv("MYSQL_USER", "spider"), password=getenv("MYSQL_PASSWORD", ""),
                           database=getenv("MYSQL_DATABASE", "spider_data"), charset="utf8mb4")


def run_monitor(pages, threshold, alerter, min_samples=1, fetcher=fetch, connector=connect):
    metrics = SpiderMetrics()  # 每轮重新创建
    books = {}
    urls = [f"https://books.toscrape.com/catalogue/page-{page}.html" for page in range(1, pages + 1)]
    with ThreadPoolExecutor(max_workers=min(3, pages)) as pool:
        futures = [pool.submit(fetcher, url) for url in urls]
        for future in as_completed(futures):
            try:
                items = future.result()
                metrics.record_request(True)
                for item in items:
                    books[item["url"]] = item
            except Exception as error:
                metrics.record_request(False)
                print("列表失败：{}".format(error))
    metrics.record_item(len(books))
    try:
        if books:
            db = connector()
            try:
                changes = Store(db).save(uuid4().hex, list(books.values()), threshold)
            finally:
                db.close()
            for book, delta in changes:
                alerter.notify(book["url"], f"{book['title']} 价格变化 {delta:+.1%}，现价 £{book['price']}")
        alert_if_needed(metrics, alerter, min_samples)
    except Exception:
        print("保存或通知失败，本轮需检查", traceback.format_exc())
        raise
    finally:
        print(metrics.summary())
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", type=int, default=1)
    parser.add_argument("--threshold", type=Decimal, default=Decimal("0.05"))
    parser.add_argument("--min-samples", type=int, default=1)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.pages <= 50 or not 0 < args.threshold <= 1 or args.min_samples < 1:
        parser.error("pages=1..50，threshold 在 (0,1]，min-samples>=1")
    alerter = Alerter(getenv("WECHAT_WEBHOOK", ""))
    def job():
        run_monitor(args.pages, args.threshold, alerter, args.min_samples)
    if args.once:
        job()
    else:
        scheduler = BlockingScheduler(timezone="UTC")
        scheduler.add_job(job, "interval", hours=1, max_instances=1, coalesce=True,
                          next_run_time=datetime.now(timezone.utc))
        scheduler.start()
