# 对应：第6章 并发编程与爬虫提速
# 小节：6.4 协程爬虫（asyncio + aiohttp）
# 条目：6.4.6 实战：高并发异步爬取图书网站
# 清单：05
# 说明：摘自书稿示例，未改写。

import aiohttp
import asyncio
from lxml import etree
import time
import json

async def fetch_page(session, page_num, semaphore):
    """异步爬取单页书籍列表"""
    if page_num == 1:
        url = 'https://books.toscrape.com/'
    else:
        url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    
    async with semaphore:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as response:
                html = await response.text()
                
                tree = etree.HTML(html)
                books_nodes = tree.xpath('//article[@class="product_pod"]')
                
                page_books = []
                for book in books_nodes:
                    title = book.xpath('.//img/@alt')[0]
                    price = book.xpath('string(.//p[@class="price_color"])').strip()
                    rating_cls = book.xpath('.//p[contains(@class,"star-rating")]/@class')[0]
                    rating = rating_cls.split()[-1]
                    link = book.xpath('.//h3/a/@href')[0]
                    
                    page_books.append({
                        'title': title,
                        'price': price,
                        'rating': rating,
                        'link': link,
                        'page': page_num
                    })
                
                return page_num, page_books, None
        
        except Exception as e:
            return page_num, [], str(e)

async def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # 该网站共 50 页
    total_pages = 50
    # 限制并发数为 10
    semaphore = asyncio.Semaphore(10)
    
    print(f"开始异步爬取，共 {total_pages} 页，并发数：10")
    start = time.time()
    
    all_books = []
    failed_pages = []
    
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [fetch_page(session, i, semaphore) for i in range(1, total_pages + 1)]
        results = await asyncio.gather(*tasks)
    
    for page_num, books, error in results:
        if error:
            failed_pages.append(page_num)
            print(f"  第 {page_num:02d} 页失败：{error}")
        else:
            all_books.extend(books)
    
    elapsed = time.time() - start
    
    print(f"\n=== 爬取完成 ===")
    print(f"总耗时：{elapsed:.2f} 秒")
    print(f"成功：{total_pages - len(failed_pages)} 页，失败：{len(failed_pages)} 页")
    print(f"共爬取书籍：{len(all_books)} 本")
    
    # 简单统计
    ratings = {}
    for book in all_books:
        ratings[book['rating']] = ratings.get(book['rating'], 0) + 1
    print(f"\n各评级分布：{ratings}")
    
    # 保存结果
    with open('books_async.json', 'w', encoding='utf-8') as f:
        json.dump(all_books, f, ensure_ascii=False, indent=2)
    print(f"\n数据已保存到 books_async.json")

asyncio.run(main())
