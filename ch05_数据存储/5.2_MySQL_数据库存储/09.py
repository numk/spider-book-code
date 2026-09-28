# 对应：第5章 数据存储
# 小节：5.2 MySQL 数据库存储
# 条目：5.2.8 删除数据
# 清单：09
# 说明：摘自书稿示例，未改写。

cursor.execute("DELETE FROM books WHERE detail_url=%s", ("https://example.com/book/1",))
