# 对应：第5章 数据存储
# 小节：5.4 PostgreSQL 数据库存储
# 条目：5.4.3 PostgreSQL 与 JSONB
# 清单：04
# 说明：摘自书稿示例，未改写。

from os import getenv
import psycopg2
from psycopg2.extras import Json

conn = psycopg2.connect(getenv("PG_DSN", "dbname=spider_db user=spider host=localhost"))
try:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS book_docs (url TEXT PRIMARY KEY, data JSONB NOT NULL)")
            cursor.execute("INSERT INTO book_docs VALUES (%s,%s) ON CONFLICT (url) DO UPDATE SET data=EXCLUDED.data",
                           ("https://example.com/book/1", Json({"title": "教学图书", "price": 79, "tags": ["Python"]})))
            cursor.execute("SELECT data->>'title' FROM book_docs WHERE data @> %s::jsonb", (Json({"tags": ["Python"]}),))
            print(cursor.fetchall())
finally:
    conn.close()
