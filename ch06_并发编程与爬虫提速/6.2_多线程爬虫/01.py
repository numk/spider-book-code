# 对应：第6章 并发编程与爬虫提速
# 小节：6.2 多线程爬虫
# 条目：6.2.1 threading 模块基础
# 清单：01
# 说明：摘自书稿示例，未改写。

import threading
import time
import requests

urls = [
    'https://httpbin.org/delay/1',  # 每个请求延迟 1 秒响应
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
]

def fetch(url, idx):
    """爬取单个 URL"""
    response = requests.get(url, timeout=10)
    print(f"[线程{idx}] 完成，状态码：{response.status_code}")

# ====== 串行执行 ======
print("=== 串行执行 ===")
start = time.time()
for i, url in enumerate(urls):
    fetch(url, i)
print(f"串行耗时：{time.time() - start:.2f} 秒\n")

# ====== 多线程执行 ======
print("=== 多线程执行 ===")
start = time.time()
threads = []
for i, url in enumerate(urls):
    t = threading.Thread(target=fetch, args=(url, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # 等待所有线程完成
print(f"多线程耗时：{time.time() - start:.2f} 秒")
