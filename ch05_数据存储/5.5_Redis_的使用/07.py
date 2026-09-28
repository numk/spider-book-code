# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.3 连接 Redis
# 清单：07
# 说明：摘自书稿示例，未改写。

import redis

# 连接到本地 Redis（无密码）
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 测试连接
print(r.ping())  # 返回 True 表示连接成功
