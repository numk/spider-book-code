# 对应：第9章 Scrapy 框架的使用
# 小节：9.6 Item Pipeline：数据管道
# 条目：9.6.4 MySQL 存储 Pipeline
# 清单：03
# 说明：摘自书稿示例，未改写。

import pymysql
from scrapy.exceptions import DropItem
SCHEMA = """CREATE TABLE IF NOT EXISTS books (
 id BIGINT AUTO_INCREMENT PRIMARY KEY,
 detail_url VARCHAR(512) CHARACTER SET ascii COLLATE ascii_bin NOT NULL UNIQUE,
 title VARCHAR(300) NOT NULL,
 author VARCHAR(100) NULL,
 price DECIMAL(10,2) NULL,
 pub_date DATE NULL,
 rating VARCHAR(20) NULL,
 upc VARCHAR(50) NULL,
 description TEXT,
 availability VARCHAR(100) NULL,
 num_reviews INT DEFAULT 0,
 crawled_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""


class MySQLPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=spider.settings.get("MYSQL_HOST", "localhost"),
            user=spider.settings.get("MYSQL_USER", "spider"),
            password=spider.settings.get("MYSQL_PASSWORD", ""),
            database=spider.settings.get("MYSQL_DATABASE", "spider_data"), charset="utf8mb4")
        self.cursor = self.conn.cursor()
        self.cursor.execute(SCHEMA)
        self.conn.commit()
        self.inserted = 0

    def process_item(self, item, spider):
        url = item.get("detail_url") or item.get("url")
        if not url or not item.get("title"):
            raise DropItem("缺少稳定 URL 或标题")
        fields = ("title", "price", "rating", "upc", "description", "availability", "num_reviews")
        values = [item.get(key) for key in fields]
        if values[-1] is None:
            values[-1] = 0
        sql = """INSERT IGNORE INTO books
          (detail_url,title,price,rating,upc,description,availability,num_reviews)
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        try:
            self.cursor.execute(sql, [url] + values)
            added = self.cursor.rowcount
            self.conn.commit()
            self.inserted += added
            spider.crawler.stats.inc_value("mysql/inserted", added)
        except Exception:
            self.conn.rollback()
            raise
        return item

    def close_spider(self, spider):
        spider.logger.info("新增书籍 %s", self.inserted)
        self.cursor.close()
        self.conn.close()
