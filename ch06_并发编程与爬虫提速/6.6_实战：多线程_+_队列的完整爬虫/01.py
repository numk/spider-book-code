# 对应：第6章 并发编程与爬虫提速
# 小节：6.6 实战：多线程 + 队列的完整爬虫
# 条目：6.4.7 小结
# 清单：01
# 说明：摘自书稿示例，未改写。

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import queue
import time
import json
from datetime import datetime

# ====== 配置 ======
BASE_URL = 'https://books.toscrape.com'
MAX_PAGES = 10
MAX_WORKERS = 5
REQUEST_DELAY = 0.5  # 每个请求之间的延迟，礼貌地对待目标网站

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# ====== 共享状态（线程安全） ======
results = []
results_lock = threading.Lock()
stats = {'success': 0, 'failed': 0, 'total_books': 0}
stats_lock = threading.Lock()

def build_url(page):
    if page == 1:
        return f'{BASE_URL}/'
    return f'{BASE_URL}/catalogue/page-{page}.html'

def fetch_and_parse(page):
    """爬取并解析单页，返回书籍列表"""
    url = build_url(page)
    
    # 礼貌延迟
    time.sleep(REQUEST_DELAY)
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        tree = etree.HTML(response.text)
        book_nodes = tree.xpath('//article[@class="product_pod"]')
        
        page_books = []
        for node in book_nodes:
            title = node.xpath('.//img/@alt')[0]
            price_str = node.xpath('string(.//p[@class="price_color"])').strip()
            price = float(price_str.replace('£', '').replace('Â', '').strip())
            rating_cls = node.xpath('.//p[contains(@class,"star-rating")]/@class')[0]
            rating = rating_cls.split()[-1]
            link = node.xpath('.//h3/a/@href')[0]
            
            page_books.append({
                'title': title,
                'price': price,
                'rating': rating,
                'detail_url': f"{BASE_URL}/catalogue/{link.lstrip('../')}",
                'page': page,
                'crawled_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        
        return page, page_books, None
    
    except requests.HTTPError as e:
        return page, [], f"HTTP错误：{e}"
    except Exception as e:
        return page, [], f"未知错误：{e}"

def process_result(page, books, error):
    """处理单页的爬取结果（线程安全）"""
    with stats_lock:
        if error:
            stats['failed'] += 1
            print(f"  [失败] 第 {page:02d} 页：{error}")
        else:
            stats['success'] += 1
            stats['total_books'] += len(books)
            print(f"  [成功] 第 {page:02d} 页：{len(books)} 本书  "
                  f"（累计成功 {stats['success']} 页，共 {stats['total_books']} 本）")
    
    if books:
        with results_lock:
            results.extend(books)

def save_to_json(data, filename):
    """保存结果到 JSON 文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n结果已保存到 {filename}")

def main():
    print("=" * 55)
    print(f"  爬虫启动")
    print(f"  目标网站：{BASE_URL}")
    print(f"  爬取页数：{MAX_PAGES} 页")
    print(f"  并发线程：{MAX_WORKERS} 个")
    print(f"  请求延迟：{REQUEST_DELAY} 秒")
    print("=" * 55)
    
    start_time = time.time()
    pages = list(range(1, MAX_PAGES + 1))
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_and_parse, page): page for page in pages}
        
        for future in as_completed(futures):
            page, books, error = future.result()
            process_result(page, books, error)
    
    elapsed = time.time() - start_time
    
    print("\n" + "=" * 55)
    print(f"  爬取完成！")
    print(f"  总耗时：   {elapsed:.2f} 秒")
    print(f"  成功页数： {stats['success']} / {MAX_PAGES}")
    print(f"  失败页数： {stats['failed']} / {MAX_PAGES}")
    print(f"  书籍总数： {stats['total_books']} 本")
    print(f"  平均速度： {stats['total_books'] / elapsed:.1f} 本/秒")
    print("=" * 55)
    
    if results:
        # 按价格排序
        results.sort(key=lambda x: x['price'])
        
        print(f"\n最便宜的5本书：")
        for book in results[:5]:
            print(f"  £{book['price']:.2f}  《{book['title'][:40]}》")
        
        print(f"\n最贵的5本书：")
        for book in results[-5:]:
            print(f"  £{book['price']:.2f}  《{book['title'][:40]}》")
        
        save_to_json(results, 'books_result.json')

if __name__ == '__main__':
    main()
