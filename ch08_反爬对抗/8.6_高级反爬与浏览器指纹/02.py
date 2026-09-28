# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.2 Cookie 和 Session 管理
# 清单：02
# 说明：摘自书稿示例，未改写。

import requests

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# 第一次请求会自动保存服务器设置的 Cookie
response = session.get('https://example.com')

# 后续请求会自动携带之前保存的 Cookie
response = session.get('https://example.com/data')
print(f"Cookie：{session.cookies.get_dict()}")
