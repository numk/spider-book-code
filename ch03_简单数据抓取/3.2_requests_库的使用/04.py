# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.4 GET和POST请求
# 清单：04
# 说明：摘自书稿示例，未改写。

import requests

url = "https://httpbin.org/get"

params = {
    "q": "spider",
    "page": 1
}

response = requests.get(url, params=params)
print(response.text)
