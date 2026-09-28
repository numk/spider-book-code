# 对应：第5章 数据存储
# 小节：5.3 MongoDB 数据库存储
# 条目：5.3.5 查询数据
# 清单：13
# 说明：摘自书稿示例，未改写。

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['spider_db']
collection = db['books']

# 查询所有文档
print("=== 所有书籍 ===")
all_books = collection.find()
for book in all_books:
    print(f"《{book['title']}》  作者：{book.get('author', '未知')}  价格：¥{book['price']}")

# 条件查询：查询价格低于 80 元的书籍
print("\n=== 价格低于80元的书籍 ===")
cheap_books = collection.find({'price': {'$lt': 80}})
for book in cheap_books:
    print(f"《{book['title']}》  ¥{book['price']}")

# 查询单条文档
print("\n=== 查询特定书籍 ===")
one_book = collection.find_one({'title': 'Python爬虫实战（第2版）'})
if one_book:
    print(f"找到：《{one_book['title']}》，标签：{one_book.get('tags', [])}")
