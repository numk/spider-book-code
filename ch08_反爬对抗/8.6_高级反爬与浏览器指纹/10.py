# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.4 TLS/JA3 指纹绕过
# 清单：10
# 说明：摘自书稿示例，未改写。

import asyncio
from curl_cffi.requests import AsyncSession

async def fetch_pages(urls: list[str]) -> list:
    async with AsyncSession(impersonate='chrome124') as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]

urls = ['https://httpbin.org/get?id=1', 'https://httpbin.org/get?id=2']
results = asyncio.run(fetch_pages(urls))
