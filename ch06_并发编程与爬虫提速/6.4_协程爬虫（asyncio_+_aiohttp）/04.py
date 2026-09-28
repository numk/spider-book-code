# 对应：第6章 并发编程与爬虫提速
# 小节：6.4 协程爬虫（asyncio + aiohttp）
# 条目：6.4.5 并发限制：Semaphore
# 清单：04
# 说明：摘自书稿示例，未改写。

import aiohttp
import asyncio
import time

async def fetch_with_semaphore(session, url, semaphore):
    """带并发限制的异步爬取"""
    async with semaphore:  # 获取信号量，超过上限则等待
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as response:
                text = await response.text()
                print(f"  完成：{url[:50]}")
                return {'url': url, 'status': response.status, 'length': len(text)}
        except Exception as e:
            print(f"  失败：{url[:50]} -> {e}")
            return {'url': url, 'status': None, 'error': str(e)}

async def main():
    # 生成 20 个待爬取 URL
    urls = [f'https://httpbin.org/delay/0?i={i}' for i in range(20)]
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    # 最多同时运行 5 个请求
    semaphore = asyncio.Semaphore(5)
    
    start = time.time()
    
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [fetch_with_semaphore(session, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)
    
    success = sum(1 for r in results if r.get('status') == 200)
    print(f"\n共 {len(urls)} 个任务，成功 {success} 个，耗时：{time.time() - start:.2f} 秒")

asyncio.run(main())
