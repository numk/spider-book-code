# 对应：第3章 简单数据抓取
# 小节：3.1 urllib 库的使用
# 条目：3.1.2 urllib 库的使用
# 清单：04
# 说明：摘自书稿示例，未改写。

from urllib.parse import urlparse

url = "http://example.com/search?q=python&page=1"

parsed_url = urlparse(url)

print(parsed_url)

host = parsed_url.netloc
path = parsed_url.path
query = parsed_url.query

print(f"Host: {host}")
print(f"Path: {path}")
print(f"Query: {query}")
