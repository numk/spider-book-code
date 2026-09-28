# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.4 TLS/JA3 指纹绕过
# 清单：09
# 说明：摘自书稿示例，未改写。

from curl_cffi.requests import Session

with Session(impersonate='chrome124') as session:
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 ...',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    })

    # 多次请求共享 TLS 指纹配置和 Cookie
    resp1 = session.get('https://www.example.com/login')
    resp2 = session.post('https://www.example.com/api/list', json={'page': 1})
    print(resp2.json())
