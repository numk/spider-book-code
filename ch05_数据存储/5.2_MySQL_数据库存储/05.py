# 对应：第5章 数据存储
# 小节：5.2 MySQL 数据库存储
# 条目：5.2.4 创建数据表
# 清单：05
# 说明：摘自书稿示例，未改写。

from db import connect, SCHEMA

db = connect()
try:
    with db.cursor() as cursor:
        cursor.execute(SCHEMA)
    db.commit()
    print("表已就绪")
finally:
    db.close()
