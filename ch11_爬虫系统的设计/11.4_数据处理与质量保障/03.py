# 对应：第11章 爬虫系统的设计
# 小节：11.4 数据处理与质量保障
# 条目：11.4.2 数据去重
# 清单：03
# 说明：摘自书稿示例，未改写。

# 复用上面的连接 connection 和 ProductItem
def save_product(item: ProductItem):
    sql = """
    INSERT IGNORE INTO products (title, price, url, rating, created_at)
    VALUES (%s, %s, %s, %s, NOW())
    """
    cursor.execute(sql, (item.title, item.price, item.url, item.rating))
