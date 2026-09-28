# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.7 响应内容的处理
# 清单：14
# 说明：摘自书稿示例，未改写。

import requests

response = requests.get("https://httpbin.org/json")
data = response.json()

print(type(data))
print(data)
