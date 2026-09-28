# 对应：第10章 分布式爬虫的设计
# 小节：10.2 分布式爬虫的核心组件
# 条目：10.2.2 URL 去重
# 清单：01
# 说明：摘自书稿示例，未改写。

import redis
import hashlib

r = redis.Redis(host="localhost", port=6379, db=0)

SEEN_KEY = "spider:seen_urls"
QUEUE_KEY = "spider:url_queue"

def add_url(url: str):
    """将 URL 加入队列（自动去重）"""
    url_hash = hashlib.md5(url.encode()).hexdigest()
    # SADD 返回 1 表示成功添加（不存在），返回 0 表示已存在
    added = r.sadd(SEEN_KEY, url_hash)
    if added:
        r.lpush(QUEUE_KEY, url)
        return True
    return False

def get_url() -> str:
    """从队列中取出一个 URL（阻塞等待）"""
    result = r.brpop(QUEUE_KEY, timeout=5)
    if result:
        _, url = result
        return url.decode()
    return None
