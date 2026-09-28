# 对应：第5章 数据存储
# 小节：5.3 MongoDB 数据库存储
# 条目：5.3.8 实战：将爬虫数据存入 MongoDB
# 清单：16
# 说明：摘自书稿示例，未改写。

import requests
from lxml import etree
import pymongo
from datetime import datetime

# MongoDB 连接配置
MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'spider_db'
COLLECTION_NAME = 'books'

def get_collection():
    """获取 MongoDB 集合对象"""
    client = pymongo.MongoClient(MONGO_URI)
    return client[DB_NAME][COLLECTION_NAME]

def save_books_to_mongo(books):
    """将书籍列表保存到 MongoDB"""
    if not books:
        return
    
    collection = get_collection()
    result = collection.insert_many(books)
    print(f"成功保存 {len(result.inserted_ids)} 条书籍数据到 MongoDB")

def crawl_and_parse():
    """爬取并解析书籍数据"""
    url = "https://books.toscrape.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    tree = etree.HTML(response.text)
    
    books = []
    items = tree.xpath('//article[@class="product_pod"]')
    
    for item in items:
        title = item.xpath('.//img/@alt')[0]
        price_str = item.xpath('string(.//p[@class="price_color"])').strip()
        price = float(price_str.replace('£', '').replace('Â', ''))
        link = item.xpath('.//h3/a/@href')[0]
        
        # MongoDB 的灵活性：可以随意添加任何字段
        books.append({
            'title': title,
            'price': price,
            'link': link,
            'source': 'books.toscrape.com',
            'crawled_at': datetime.now(),   # 存储爬取时间
            'tags': [],                      # 预留标签字段
        })
    
    return books

if __name__ == '__main__':
    print("开始爬取...")
    books = crawl_and_parse()
    print(f"爬取到 {len(books)} 本书，开始存储...")
    save_books_to_mongo(books)
    
    # 验证：从 MongoDB 查询并打印前5条
    collection = get_collection()
    print("\n=== 数据库中的前5条记录 ===")
    for book in collection.find().limit(5):
        print(f"《{book['title']}》  ¥{book['price']}  爬取时间：{book['crawled_at'].strftime('%Y-%m-%d %H:%M')}")
