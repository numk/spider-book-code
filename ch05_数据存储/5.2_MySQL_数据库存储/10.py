# 对应：第5章 数据存储
# 小节：5.2 MySQL 数据库存储
# 条目：5.2.9 实战：列表采集与 MySQL 存储
# 清单：10
# 说明：摘自书稿示例，未改写。

from urllib.parse import urljoin
from decimal import Decimal
import requests
from bs4 import BeautifulSoup
from db import connect, SCHEMA

UPSERT = """INSERT INTO books (detail_url,title,price,pub_date)
 VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE
 title=%s, price=%s, crawled_at=CURRENT_TIMESTAMP"""


def collect():
    url = "https://books.toscrape.com/"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    response.encoding = "utf-8"
    books = []
    for card in BeautifulSoup(response.text, "html.parser").select("article.product_pod"):
        link, amount = card.select_one("h3 a"), card.select_one(".price_color")
        if link is None or amount is None or not link.get("href") or not link.get("title"):
            raise ValueError("缺少书籍字段")
        title = link["title"]
        price = Decimal(amount.get_text(strip=True).removeprefix("£"))
        books.append((urljoin(url, link["href"]), title, price, None, title, price))
    if not books:
        raise ValueError("书籍列表为空")
    return books


if __name__ == "__main__":
    rows = collect()
    db = connect()
    try:
        with db.cursor() as cursor:
            cursor.execute(SCHEMA)
            cursor.executemany(UPSERT, rows)
            affected = cursor.rowcount
        db.commit()
        print("处理 {} 本书，数据库受影响行数 {}".format(len(rows), affected))
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
