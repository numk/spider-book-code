# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.7 Hash 哈希操作：存储结构化数据
# 清单：17
# 说明：摘自书稿示例，未改写。

import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 存储一本书的信息
book_key = 'book:1001'
r.hset(book_key, mapping={
    'title': 'Python爬虫实战（第2版）',
    'author': '范传辉',
    'price': '79.00',
    'pub_date': '2025-03-15'
})
# 设置 1 小时后过期
r.expire(book_key, 3600)

# 获取单个字段
title = r.hget(book_key, 'title')
print(f"书名：{title}")

# 获取所有字段
book_info = r.hgetall(book_key)
print(f"完整信息：{book_info}")

# 更新单个字段（不影响其他字段）
r.hset(book_key, 'price', '69.00')
print(f"更新后价格：{r.hget(book_key, 'price')}")
