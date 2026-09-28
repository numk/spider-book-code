# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.5 请求头
# 清单：08
# 说明：摘自书稿示例，未改写。

import requests

url = "https://httpbin.org/get"

headers = {
    'User-Agent': 'spider/2025'
}

response = requests.get(url, headers=headers)
print(response.text)
