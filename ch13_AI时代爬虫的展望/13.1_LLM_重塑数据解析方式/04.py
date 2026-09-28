# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.1 LLM 重塑数据解析方式
# 条目：13.1.4 专为爬虫设计的 LLM 解析库
# 清单：04
# 说明：摘自书稿示例，未改写。

# pip install crawl4ai
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig, CacheMode
from os import getenv
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from pydantic import BaseModel

class Article(BaseModel):
    title: str
    author: str
    publish_date: str
    content: str
    tags: list[str]

async def main():
    strategy = LLMExtractionStrategy(
        llm_config=LLMConfig(provider='openai/gpt-4o-mini', api_token=getenv('OPENAI_API_KEY')),
        schema=Article.model_json_schema(),
        instruction='从文章页面中提取结构化内容',
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url='https://example.com/article/123',
            config=CrawlerRunConfig(
                extraction_strategy=strategy, cache_mode=CacheMode.BYPASS)
        )
        
        import json
        articles = json.loads(result.extracted_content)
        print(articles)

asyncio.run(main())
