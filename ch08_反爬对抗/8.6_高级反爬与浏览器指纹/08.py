# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.4 TLS/JA3 指纹绕过
# 清单：08
# 说明：摘自书稿示例，未改写。

from curl_cffi import requests as cffi_requests

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/124.0.0.0 Safari/537.36'
    ),
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://www.example.com/',
}

proxies = {
    'http': 'http://your-proxy:8080',
    'https': 'http://your-proxy:8080',
}

response = cffi_requests.get(
    'https://www.example.com/api/data',
    headers=headers,
    proxies=proxies,
    impersonate='chrome124',
    timeout=15,
)
print(response.json())
