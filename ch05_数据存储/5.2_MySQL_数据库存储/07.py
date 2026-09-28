# 对应：第5章 数据存储
# 小节：5.2 MySQL 数据库存储
# 条目：5.2.6 查询数据
# 清单：07
# 说明：摘自书稿示例，未改写。

cursor.execute("SELECT title,price,pub_date FROM books WHERE price < %s", (80,))
rows = cursor.fetchall()
