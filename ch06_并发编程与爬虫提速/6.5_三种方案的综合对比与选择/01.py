# 对应：第6章 并发编程与爬虫提速
# 小节：6.5 三种方案的综合对比与选择
# 条目：6.4.7 小结
# 清单：01
# 说明：摘自书稿示例，未改写。

import requests
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import time

TARGET_URLS = [f'https://books.toscrape.com/catalogue/page-{i}.html' for i in range(1, 21)]
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# ====== 方案一：串行 ======
def serial_crawl():
    results = []
    for url in TARGET_URLS:
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            results.append(len(r.text))
        except:
            results.append(0)
    return results

# ====== 方案二：多线程 ======
def fetch_sync(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        return len(r.text)
    except:
        return 0

def thread_crawl():
    with ThreadPoolExecutor(max_workers=10) as executor:
        return list(executor.map(fetch_sync, TARGET_URLS))

# ====== 方案三：协程 ======
async def fetch_async(session, url, sem):
    async with sem:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as r:
                text = await r.text()
                return len(text)
        except:
            return 0

async def async_crawl():
    sem = asyncio.Semaphore(10)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        tasks = [fetch_async(session, url, sem) for url in TARGET_URLS]
        return await asyncio.gather(*tasks)

if __name__ == '__main__':
    print(f"目标：爬取 {len(TARGET_URLS)} 个页面\n")
    
    print("测试串行...")
    t = time.time()
    serial_crawl()
    print(f"串行耗时：    {time.time() - t:.2f} 秒")
    
    print("测试多线程...")
    t = time.time()
    thread_crawl()
    print(f"多线程耗时：  {time.time() - t:.2f} 秒")
    
    print("测试协程...")
    t = time.time()
    asyncio.run(async_crawl())
    print(f"协程耗时：    {time.time() - t:.2f} 秒")
