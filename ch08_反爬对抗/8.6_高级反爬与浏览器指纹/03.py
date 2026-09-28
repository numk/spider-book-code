# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.2 Cookie 和 Session 管理
# 清单：03
# 说明：摘自书稿示例，未改写。

import requests

session = requests.Session()

# 从浏览器 Network 面板中复制的 Cookie 字符串，解析并设置
cookie_str = 'sessionid=abc123; user_id=12345; _csrf=xyz789'
for item in cookie_str.split('; '):
    key, value = item.split('=', 1)
    session.cookies.set(key.strip(), value.strip())

response = session.get('https://example.com/protected')
print(response.status_code)
