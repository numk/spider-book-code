# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.7 响应内容的处理
# 清单：13
# 说明：摘自书稿示例，未改写。

import requests

image_url = "https://httpbin.org/image/png"
response = requests.get(image_url)

with open("demo.png", "wb") as f:
    f.write(response.content)
