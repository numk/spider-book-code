# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.5 Set 集合操作：URL 去重
# 清单：12
# 说明：摘自书稿示例，未改写。

import redis
import hashlib

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def url_to_fingerprint(url):
    """将 URL 转换为 MD5 指纹，节省存储空间"""
    return hashlib.md5(url.encode()).hexdigest()

def is_crawled(url):
    """检查 URL 是否已经爬取过"""
    fp = url_to_fingerprint(url)
    return r.sismember('spider:visited_urls', fp)

def mark_as_crawled(url):
    """将 URL 标记为已爬取"""
    fp = url_to_fingerprint(url)
    r.sadd('spider:visited_urls', fp)

# 模拟爬虫的 URL 去重流程
urls_to_crawl = [
    'https://example.com/book/1',
    'https://example.com/book/2',
    'https://example.com/book/1',  # 重复 URL
    'https://example.com/book/3',
    'https://example.com/book/2',  # 重复 URL
]

for url in urls_to_crawl:
    if is_crawled(url):
        print(f"[跳过] 已爬取：{url}")
    else:
        print(f"[爬取] 正在爬取：{url}")
        # 这里放实际的爬取逻辑...
        mark_as_crawled(url)

# 查看已爬取 URL 数量
count = r.scard('spider:visited_urls')
print(f"\n共爬取了 {count} 个不重复的 URL")
