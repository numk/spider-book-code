# 对应：第5章 数据存储
# 小节：5.2 MySQL 数据库存储
# 条目：5.2.5 插入、批量写入与回滚
# 清单：06
# 说明：摘自书稿示例，未改写。

from decimal import Decimal
from db import connect

sql = '''INSERT INTO books (detail_url,title,price) VALUES (%s,%s,%s)
 ON DUPLICATE KEY UPDATE title=%s, price=%s, crawled_at=CURRENT_TIMESTAMP'''
rows = [("https://example.com/book/1", "教学图书", Decimal("79.00"), "教学图书", Decimal("79.00"))]
db = connect()
try:
    with db.cursor() as cursor:
        cursor.execute(sql, rows[0])
        cursor.executemany(sql, rows)
        print("受影响行数 {}".format(cursor.rowcount))
    db.commit()
except Exception:
    db.rollback()
    raise
finally:
    db.close()
