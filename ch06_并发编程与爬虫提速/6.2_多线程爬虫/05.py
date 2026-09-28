# 对应：第6章 并发编程与爬虫提速
# 小节：6.2 多线程爬虫
# 条目：6.2.4 实战：多线程爬取图书网站
# 清单：05
# 说明：摘自书稿示例，未改写。

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import threading

# 线程安全的结果收集
results = []
results_lock = threading.Lock()

def fetch_page(page_num):
    """爬取指定页码的图书列表"""
    if page_num == 1:
        url = 'https://books.toscrape.com/'
    else:
        url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        tree = etree.HTML(response.text)
        books = tree.xpath('//article[@class="product_pod"]')
        
        page_results = []
        for book in books:
            title = book.xpath('.//img/@alt')[0]
            price = book.xpath('string(.//p[@class="price_color"])').strip()
            rating_class = book.xpath('.//p[contains(@class,"star-rating")]/@class')[0]
            rating = rating_class.split()[-1]
            
            page_results.append({
                'title': title,
                'price': price,
                'rating': rating,
                'page': page_num
            })
        
        return page_num, page_results, None
    
    except Exception as e:
        return page_num, [], str(e)

def save_results(page_num, books):
    """线程安全地将结果追加到总列表"""
    with results_lock:
        results.extend(books)
        print(f"  第 {page_num:02d} 页完成，获取 {len(books)} 本书，累计 {len(results)} 本")

# ====== 串行版本（对照） ======
print("=== 串行爬取（前5页）===")
start = time.time()
for i in range(1, 6):
    page_num, books, err = fetch_page(i)
    if not err:
        print(f"  第 {page_num} 页：{len(books)} 本书")
serial_time = time.time() - start
print(f"串行耗时：{serial_time:.2f} 秒\n")

# ====== 多线程版本 ======
results.clear()
print("=== 多线程爬取（前10页）===")
start = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(fetch_page, i): i for i in range(1, 11)}
    
    for future in as_completed(futures):
        page_num, books, err = future.result()
        if err:
            print(f"  第 {page_num} 页爬取失败：{err}")
        else:
            save_results(page_num, books)

thread_time = time.time() - start
print(f"\n多线程耗时：{thread_time:.2f} 秒")
print(f"共爬取 {len(results)} 本书籍信息")

# 打印前5条
print("\n=== 部分结果预览 ===")
for book in results[:5]:
    print(f"《{book['title'][:30]}》  {book['price']}  评级：{book['rating']}  (第{book['page']}页)")
