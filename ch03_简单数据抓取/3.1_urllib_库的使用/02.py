# 对应：第3章 简单数据抓取
# 小节：3.1 urllib 库的使用
# 条目：3.1.2 urllib 库的使用
# 清单：02
# 说明：摘自书稿示例，未改写。

from urllib.parse import urlencode

base_url = "http://example.com/search"

params = {
    "q": "python",
    "page": 1
}

query_string = urlencode(params)
full_url = f"{base_url}?{query_string}"

print(full_url)
