# 对应：第3章 简单数据抓取
# 小节：3.3 httpx 库的使用
# 条目：3.3.3 异步用法（AsyncClient）
# 清单：05
# 说明：摘自书稿示例，未改写。

import asyncio
import httpx

async def fetch(url: str) -> dict:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url)
        return response.json()

result = asyncio.run(fetch('https://httpbin.org/get'))
print(result)
