# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.9 Cookie 与 Session
# 清单：18
# 说明：摘自书稿示例，未改写。

import requests

url = "https://httpbin.org/cookies"

cookies = {
    "token": "123456",
    "name": "spider"
}

response = requests.get(url, cookies=cookies)
print(response.text)
