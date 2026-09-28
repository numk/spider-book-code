# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.6 List 列表操作：URL 爬取队列
# 清单：14
# 说明：摘自书稿示例，未改写。

import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# ====== 生产者：将待爬取的 URL 加入队列 ======
def add_urls_to_queue(urls):
    """将 URL 列表推入爬取队列"""
    for url in urls:
        r.rpush('spider:url_queue', url)  # 从右端推入
    print(f"已将 {len(urls)} 个 URL 加入队列")

# ====== 消费者：从队列中取出 URL 进行爬取 ======
def get_url_from_queue():
    """从爬取队列中取出一个 URL"""
    url = r.lpop('spider:url_queue')  # 从左端弹出
    return url

def get_queue_length():
    """获取队列中待爬取的 URL 数量"""
    return r.llen('spider:url_queue')

# 模拟生产者：添加 URL
seed_urls = [
    'https://example.com/page/1',
    'https://example.com/page/2',
    'https://example.com/page/3',
    'https://example.com/page/4',
    'https://example.com/page/5',
]
add_urls_to_queue(seed_urls)
print(f"队列中共有 {get_queue_length()} 个待爬取 URL")

# 模拟消费者：逐个取出并处理
print("\n开始消费队列：")
while True:
    url = get_url_from_queue()
    if url is None:
        print("队列已空，爬取完成！")
        break
    print(f"正在爬取：{url}  （剩余：{get_queue_length()} 个）")
    # 这里放实际的爬取逻辑...
