# 对应：第4章 数据解析
# 小节：4.4 JSON 数据解析
# 条目：4.4.5 实战：爬取 API 接口的 JSON 数据
# 清单：05
# 说明：摘自书稿示例，未改写。

import requests
import json

# HTTP 请求回显接口
url = "https://httpbin.org/anything"

# 构造请求参数
payload = {
    "action": "search",
    "keyword": "Python",
    "category": "编程",
    "page": 1,
    "page_size": 10
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Content-Type': 'application/json',
    'Referer': 'https://www.example.com/books'
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("请求成功！")
    print(f"回显请求体：{data.get('json', {})}")
else:
    print(f"请求失败，状态码：{response.status_code}")
