# 对应：第5章 数据存储
# 小节：5.2 MySQL 数据库存储
# 条目：5.2.3 统一连接配置
# 清单：04
# 说明：摘自书稿示例，未改写。

from os import getenv
import pymysql

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


def connect():
    return pymysql.connect(host=getenv("MYSQL_HOST", "localhost"),
                           user=getenv("MYSQL_USER", "spider"),
                           password=getenv("MYSQL_PASSWORD", ""),
                           database=getenv("MYSQL_DATABASE", "spider_data"), charset="utf8mb4")
