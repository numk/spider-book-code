# 对应：第8章 反爬对抗
# 小节：8.3 IP 封禁与代理 IP
# 条目：8.3.4 代理 IP 池的实现
# 清单：04
# 说明：摘自书稿示例，未改写。

import requests
import random
import time

# 代理 IP 列表（实际使用时替换为真实可用的代理）
PROXY_LIST = [
    'http://用户名:密码@代理IP1:端口',
    'http://用户名:密码@代理IP2:端口',
    'http://用户名:密码@代理IP3:端口',
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def get_random_proxy():
    """随机获取一个代理"""
    proxy_url = random.choice(PROXY_LIST)
    return {'http': proxy_url, 'https': proxy_url}

def fetch_with_retry(url, max_retries=3):
    """带重试的请求，失败自动换代理"""
    for attempt in range(max_retries):
        proxy = get_random_proxy()
        try:
            response = requests.get(
                url,
                proxies=proxy,
                headers=HEADERS,
                timeout=10
            )
            if response.status_code == 200:
                return response
            elif response.status_code == 403:
                print(f"  [第{attempt+1}次] IP 被封禁（403），切换代理...")
            elif response.status_code == 429:
                print(f"  [第{attempt+1}次] 请求频率过高（429），等待后重试...")
                time.sleep(5)
        except requests.exceptions.ProxyError:
            print(f"  [第{attempt+1}次] 代理连接失败，切换代理...")
        except requests.exceptions.Timeout:
            print(f"  [第{attempt+1}次] 请求超时，切换代理...")
    
    print(f"  已重试 {max_retries} 次，放弃该 URL")
    return None

# 使用示例
urls = [
    'https://httpbin.org/ip',
    'https://httpbin.org/get',
    'https://httpbin.org/headers',
]

for url in urls:
    print(f"请求：{url}")
    response = fetch_with_retry(url)
    if response:
        print(f"  成功，状态码：{response.status_code}")
    time.sleep(random.uniform(1, 2))
