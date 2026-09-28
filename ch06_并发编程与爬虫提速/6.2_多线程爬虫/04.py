# 对应：第6章 并发编程与爬虫提速
# 小节：6.2 多线程爬虫
# 条目：6.2.3 线程池：ThreadPoolExecutor
# 清单：04
# 说明：摘自书稿示例，未改写。

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import time

def fetch_page(url):
    """爬取单个页面，返回 (url, 状态码, 内容长度)"""
    try:
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        return url, response.status_code, len(response.text)
    except Exception as e:
        return url, None, str(e)

urls = [
    'https://www.baidu.com',
    'https://www.bing.com',
    'https://httpbin.org/get',
    'https://httpbin.org/ip',
    'https://httpbin.org/headers',
    'https://httpbin.org/user-agent',
]

start = time.time()

# 使用线程池，最多同时运行 4 个线程
with ThreadPoolExecutor(max_workers=4) as executor:
    # submit() 提交任务，返回 Future 对象
    futures = {executor.submit(fetch_page, url): url for url in urls}
    
    # as_completed() 哪个任务先完成就先处理哪个
    for future in as_completed(futures):
        url, status, length = future.result()
        if status:
            print(f"✓ {url[:40]:<40} 状态：{status}  内容长度：{length} 字符")
        else:
            print(f"✗ {url[:40]:<40} 失败：{length}")

print(f"\n总耗时：{time.time() - start:.2f} 秒")
