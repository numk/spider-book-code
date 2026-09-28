# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.4 GET和POST请求
# 清单：07
# 说明：摘自书稿示例，未改写。

import requests
import json

url = "https://httpbin.org/post"

json_data = {
    "q": ["spider", "python"],
    "page": 1,
    "method": "post"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(json_data), headers=headers)
print(response.text)
