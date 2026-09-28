# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.9 Cookie 与 Session
# 清单：17
# 说明：摘自书稿示例，未改写。

import requests

session = requests.Session()

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/135.0.0.0 Safari/537.36"
    )
}

response1 = session.get("https://httpbin.org/cookies/set/name/spider", headers=headers)
print("第一次请求后的 cookies:", session.cookies.get_dict())

response2 = session.get("https://httpbin.org/cookies", headers=headers)
print(response2.text)
