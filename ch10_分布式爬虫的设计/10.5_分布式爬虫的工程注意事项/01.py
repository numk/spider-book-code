# 对应：第10章 分布式爬虫的设计
# 小节：10.5 分布式爬虫的工程注意事项
# 条目：10.5.1 任务分配策略
# 清单：01
# 说明：摘自书稿示例，未改写。

# 推入高优先级 URL（分数越小越先被取出）
r.zadd("spider:priority_queue", {"https://example.com/hot-page": 1})

# 推入普通 URL
r.zadd("spider:priority_queue", {"https://example.com/normal-page": 10})

# 取出优先级最高的 URL
result = r.zpopmin("spider:priority_queue", count=1)
