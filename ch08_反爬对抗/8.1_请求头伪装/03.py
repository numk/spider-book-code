# 对应：第8章 反爬对抗
# 小节：8.1 请求头伪装
# 条目：8.1.2 完善请求头字段
# 清单：03
# 说明：摘自书稿示例，未改写。

import requests

url = 'https://httpbin.org/headers'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.google.com/',   # 表示从 Google 搜索跳转而来
    'Cache-Control': 'max-age=0',
}

response = requests.get(url, headers=headers)
print(response.json())
