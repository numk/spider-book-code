# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.6 新协议与技术趋势
# 条目：13.6.1 HTTP/3 与 QUIC 协议
# 清单：01
# 说明：摘自书稿示例，未改写。

# pip install "httpx[http2]"
import httpx
import asyncio

async def fetch_with_http2(url: str):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(f"HTTP/{response.http_version}  {response.status_code}")
        return response.text

asyncio.run(fetch_with_http2('https://www.cloudflare.com'))
