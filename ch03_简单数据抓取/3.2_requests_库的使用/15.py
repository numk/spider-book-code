# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.7 响应内容的处理
# 清单：15
# 说明：摘自书稿示例，未改写。

import requests

response = requests.get("https://www.baidu.com")

print(response.status_code)   # 状态码
print(response.url)           # 实际访问的 URL
print(response.headers)       # 响应头
print(response.cookies)       # 响应中的 cookies
