# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.2 Web Agent：爬虫的智能化升维
# 条目：13.2.4 MCP（Model Context Protocol）：爬虫工具化的新范式
# 清单：03
# 说明：摘自书稿示例，未改写。

# 一个简单的爬虫 MCP Server 示例
# pip install mcp requests beautifulsoup4
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types
import requests
from bs4 import BeautifulSoup

app = Server("web-scraper")

@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="scrape_url",
            description="爬取指定 URL 的网页内容，返回清理后的文本",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "要爬取的网页 URL"},
                    "selector": {"type": "string", "description": "可选的 CSS 选择器，用于提取特定区域"},
                },
                "required": ["url"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "scrape_url":
        url = arguments["url"]
        selector = arguments.get("selector")
        
        headers = {'User-Agent': 'Mozilla/5.0 ...'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if selector:
            element = soup.select_one(selector)
            text = element.get_text(strip=True) if element else "未找到匹配元素"
        else:
            for tag in soup(['script', 'style']):
                tag.decompose()
            text = soup.get_text(separator='\n', strip=True)
        
        return [types.TextContent(type="text", text=text[:5000])]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
