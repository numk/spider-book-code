# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.3 连接 Redis
# 清单：09
# 说明：摘自书稿示例，未改写。

r = redis.Redis(host='localhost', port=6379, password='your_password', db=0, decode_responses=True)
