# 对应：第3章 简单数据抓取
# 小节：3.3 httpx 库的使用
# 条目：3.3.3 异步用法（AsyncClient）
# 清单：06
# 说明：摘自书稿示例，未改写。

import asyncio
import httpx

async def fetch_all(urls: list[str]) -> list:
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]

urls = [
    'https://httpbin.org/get?id=1',
    'https://httpbin.org/get?id=2',
    'https://httpbin.org/get?id=3',
]

results = asyncio.run(fetch_all(urls))
for r in results:
    print(r['args'])
