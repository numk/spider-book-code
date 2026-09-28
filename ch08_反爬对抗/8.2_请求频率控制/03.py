# 对应：第8章 反爬对抗
# 小节：8.2 请求频率控制
# 条目：8.1.2 完善请求头字段
# 清单：03
# 说明：摘自书稿示例，未改写。

from concurrent.futures import ThreadPoolExecutor
import requests
import time
import random

def fetch(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    response = requests.get(url, headers=headers, timeout=10)
    time.sleep(random.uniform(0.5, 1.5))  # 每个线程请求后随机延迟
    return response.status_code

urls = [f'https://httpbin.org/delay/0?i={i}' for i in range(10)]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch, urls))

print(f"全部完成：{results}")
