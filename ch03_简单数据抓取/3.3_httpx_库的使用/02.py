# 对应：第3章 简单数据抓取
# 小节：3.3 httpx 库的使用
# 条目：3.3.2 同步用法
# 清单：02
# 说明：摘自书稿示例，未改写。

import httpx

# GET 请求
response = httpx.get(
    'https://httpbin.org/get',
    params={'keyword': 'python', 'page': 1},
    headers={'User-Agent': 'Mozilla/5.0'},
    timeout=10,
)
print(response.status_code)   # 200
print(response.json())

# POST 请求（发送 JSON）
response = httpx.post(
    'https://httpbin.org/post',
    json={'username': 'test', 'password': '123456'},
    timeout=10,
)
print(response.json())
