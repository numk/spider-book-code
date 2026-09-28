# 对应：第4章 数据解析
# 小节：4.4 JSON 数据解析
# 条目：4.4.4 requests 库直接解析 JSON
# 清单：03
# 说明：摘自书稿示例，未改写。

import requests

url = "https://httpbin.org/get"

params = {
    "keyword": "Python",
    "page": 1
}

response = requests.get(url, params=params)

# 直接解析 JSON 响应
data = response.json()

print(type(data))
print(data['args'])
