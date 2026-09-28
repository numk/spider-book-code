# 对应：第6章 并发编程与爬虫提速
# 小节：6.3 多进程爬虫
# 条目：6.3.4 实战：多进程分网站爬取
# 清单：03
# 说明：摘自书稿示例，未改写。

from multiprocessing import Process, Manager
import requests
from lxml import etree
import time

def crawl_site(site_name, base_url, pages, shared_results):
    """每个进程负责爬取一个网站的多个页面"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    site_results = []
    
    for page in range(1, pages + 1):
        url = f"{base_url}{page}.html" if page > 1 else base_url
        try:
            response = requests.get(url, headers=headers, timeout=10)
            tree = etree.HTML(response.text)
            books = tree.xpath('//article[@class="product_pod"]')
            
            for book in books:
                title = book.xpath('.//img/@alt')[0]
                price = book.xpath('string(.//p[@class="price_color"])').strip()
                site_results.append({
                    'site': site_name,
                    'title': title,
                    'price': price,
                    'page': page
                })
            
            print(f"[{site_name}] 第 {page} 页完成，共 {len(books)} 条")
        except Exception as e:
            print(f"[{site_name}] 第 {page} 页失败：{e}")
    
    # 将结果写入共享列表
    shared_results[site_name] = site_results
    print(f"[{site_name}] 全部完成，共 {len(site_results)} 条记录")

if __name__ == '__main__':
    start = time.time()
    
    # Manager 提供了可以跨进程共享的数据结构
    with Manager() as manager:
        shared_results = manager.dict()
        
        # 启动两个进程分别爬取不同页码范围
        p1 = Process(
            target=crawl_site,
            args=('任务A-前3页', 'https://books.toscrape.com/catalogue/page-', 3, shared_results)
        )
        p2 = Process(
            target=crawl_site,
            args=('任务B-后3页', 'https://books.toscrape.com/catalogue/page-', 3, shared_results)
        )
        
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        
        # 汇总结果
        total = sum(len(v) for v in shared_results.values())
        print(f"\n总耗时：{time.time() - start:.2f} 秒，共爬取 {total} 条数据")
