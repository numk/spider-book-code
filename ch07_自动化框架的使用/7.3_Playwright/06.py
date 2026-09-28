# 对应：第7章 自动化框架的使用
# 小节：7.3 Playwright
# 条目：7.3.5 异步模式（高并发爬取）
# 清单：06
# 说明：摘自书稿示例，未改写。

import asyncio
from playwright.async_api import async_playwright
import time

async def scrape_page(browser, url, page_id):
    """异步爬取单个页面"""
    page = await browser.new_page()
    try:
        await page.goto(url, timeout=15000)
        await page.wait_for_load_state('domcontentloaded')
        
        title = await page.title()
        content_length = len(await page.content())
        print(f"[页面{page_id}] 标题：{title[:30]}  内容长度：{content_length}")
        return {'url': url, 'title': title, 'length': content_length}
    except Exception as e:
        print(f"[页面{page_id}] 失败：{e}")
        return {'url': url, 'error': str(e)}
    finally:
        await page.close()

async def main():
    urls = [
        'https://www.baidu.com',
        'https://www.bing.com',
        'https://httpbin.org/get',
        'https://httpbin.org/ip',
        'https://httpbin.org/headers',
    ]
    
    start = time.time()
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # 并发爬取所有页面
        tasks = [scrape_page(browser, url, i+1) for i, url in enumerate(urls)]
        results = await asyncio.gather(*tasks)
        
        await browser.close()
    
    print(f"\n总耗时：{time.time() - start:.2f} 秒")
    return results

asyncio.run(main())
