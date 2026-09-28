# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.3 requests 库的使用
# 清单：03
# 说明：摘自书稿示例，未改写。

import requests

response = requests.post('https://httpbin.org/post')
response = requests.put('https://httpbin.org/put')
response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/head')
response = requests.options('https://httpbin.org/options')
