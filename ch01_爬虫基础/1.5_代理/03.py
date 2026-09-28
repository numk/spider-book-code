# 对应：第1章 爬虫基础
# 小节：1.5 代理
# 条目：1.5.4 代理的使用方式
# 清单：03
# 说明：摘自书稿示例，未改写。

import requests

proxies = {
    'http': 'http://代理IP:端口',
    'https': 'http://代理IP:端口',
}

response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
print(response.json())
