# 对应：第6章 并发编程与爬虫提速
# 小节：6.4 协程爬虫（asyncio + aiohttp）
# 条目：6.4.4 基本异步爬取
# 清单：03
# 说明：摘自书稿示例，未改写。

import aiohttp
import asyncio
import time

async def fetch(session, url):
    """异步爬取单个 URL"""
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            text = await response.text()
            return url, response.status, len(text)
    except Exception as e:
        return url, None, str(e)

async def main():
    urls = [
        'https://httpbin.org/get',
        'https://httpbin.org/ip',
        'https://httpbin.org/headers',
        'https://httpbin.org/user-agent',
        'https://httpbin.org/uuid',
        'https://www.baidu.com',
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    start = time.time()
    
    # 创建一个可复用的 Session（类似 requests.Session），性能更好
    async with aiohttp.ClientSession(headers=headers) as session:
        # 并发发起所有请求
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    for url, status, content in results:
        if status:
            print(f"✓ [{status}] {url[:45]:<45} 内容长度：{content}")
        else:
            print(f"✗ [失败] {url[:45]:<45} 错误：{content}")
    
    print(f"\n总耗时：{time.time() - start:.2f} 秒")

asyncio.run(main())
