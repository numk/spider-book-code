# 对应：第5章 数据存储
# 小节：5.2 MySQL 数据库存储
# 条目：5.2.7 更新数据
# 清单：08
# 说明：摘自书稿示例，未改写。

cursor.execute("UPDATE books SET price=%s WHERE detail_url=%s", (69, "https://example.com/book/1"))
