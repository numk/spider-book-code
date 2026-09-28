# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.4 String 字符串操作
# 清单：10
# 说明：摘自书稿示例，未改写。

import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 设置键值对
r.set('spider:name', 'Python爬虫')
r.set('spider:version', '2.0')

# 获取值
name = r.get('spider:name')
print(f"爬虫名称：{name}")

# 设置带过期时间的缓存（单位：秒），60 秒后自动删除
r.set('page:cache:url_001', '<html>...</html>', ex=60)

# 查看剩余过期时间（秒）
ttl = r.ttl('page:cache:url_001')
print(f"缓存剩余有效期：{ttl} 秒")

# 自增计数器（原子操作）
r.set('spider:crawled_count', 0)
r.incr('spider:crawled_count')  # +1
r.incr('spider:crawled_count')  # +1
r.incrby('spider:crawled_count', 10)  # +10
count = r.get('spider:crawled_count')
print(f"已爬取页面数：{count}")

# 删除键
r.delete('spider:version')
