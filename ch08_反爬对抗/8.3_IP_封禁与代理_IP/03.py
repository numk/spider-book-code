# 对应：第8章 反爬对抗
# 小节：8.3 IP 封禁与代理 IP
# 条目：8.3.3 在 requests 中使用代理 IP
# 清单：03
# 说明：摘自书稿示例，未改写。

import requests

# 快代理隧道代理示例（需要替换为你自己的账号信息）
proxy_host = 'proxy.kuaidaili.com'
proxy_port = '15818'
proxy_user = 'your_username'
proxy_pass = 'your_password'

proxies = {
    'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

try:
    response = requests.get(
        'https://httpbin.org/ip',
        proxies=proxies,
        headers=headers,
        timeout=10
    )
    print(f"当前出口 IP：{response.json()}")
except requests.exceptions.ProxyError as e:
    print(f"代理连接失败：{e}")
