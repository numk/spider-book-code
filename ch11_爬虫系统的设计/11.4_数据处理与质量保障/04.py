# 对应：第11章 爬虫系统的设计
# 小节：11.4 数据处理与质量保障
# 条目：11.4.2 数据去重
# 清单：04
# 说明：摘自书稿示例，未改写。

sql = """
INSERT INTO products (title, price, url, rating, updated_at)
VALUES (%s, %s, %s, %s, NOW())
ON DUPLICATE KEY UPDATE
    price = VALUES(price),
    rating = VALUES(rating),
    updated_at = NOW()
"""
