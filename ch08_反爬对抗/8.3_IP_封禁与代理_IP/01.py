# 对应：第8章 反爬对抗
# 小节：8.3 IP 封禁与代理 IP
# 条目：8.3.3 在 requests 中使用代理 IP
# 清单：01
# 说明：摘自书稿示例，未改写。

import requests

# 格式：{'协议': '协议://IP:端口'}
proxies = {
    'http': 'http://127.0.0.1:7890',    # HTTP 代理
    'https': 'http://127.0.0.1:7890',   # HTTPS 代理
}

response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
print(response.json())
