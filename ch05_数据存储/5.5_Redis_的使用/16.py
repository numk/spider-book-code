# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.6 List 列表操作：URL 爬取队列
# 清单：16
# 说明：摘自书稿示例，未改写。

# 阻塞式弹出，最多等待 30 秒
result = r.blpop('spider:url_queue', timeout=30)
if result:
    _, url = result  # result 是 (队列名, 值) 的元组
    print(f"取到 URL：{url}")
