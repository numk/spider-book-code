# 对应：第3章 简单数据抓取
# 小节：3.3 httpx 库的使用
# 条目：3.3.2 同步用法
# 清单：03
# 说明：摘自书稿示例，未改写。

import httpx

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

with httpx.Client(headers=headers, timeout=10) as client:
    # 第一次请求（模拟登录）
    resp = client.post('https://httpbin.org/post', data={'user': 'alice'})
    print('登录响应:', resp.status_code)

    # 后续请求自动携带 Cookie 和公共请求头
    resp = client.get('https://httpbin.org/cookies')
    print('Cookie 状态:', resp.json())
