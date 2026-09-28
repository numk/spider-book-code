# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.6 抓取网页
# 清单：10
# 说明：摘自书稿示例，未改写。

import requests

url = "https://www.baidu.com"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/135.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding

print(response.text[:500])
