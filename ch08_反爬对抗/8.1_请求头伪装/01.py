# 对应：第8章 反爬对抗
# 小节：8.1 请求头伪装
# 条目：8.1.1 User-Agent 伪装
# 清单：01
# 说明：摘自书稿示例，未改写。

import requests

url = 'https://httpbin.org/user-agent'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
print(response.json())
