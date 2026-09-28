# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.3 requests 库的使用
# 清单：02
# 说明：摘自书稿示例，未改写。

import requests

url = "https://www.baidu.com"
response = requests.get(url)
print(type(response))
print(response.status_code)
print(response.headers)
print(response.text[:100])
print(response.cookies)
