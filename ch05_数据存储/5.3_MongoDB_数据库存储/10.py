# 对应：第5章 数据存储
# 小节：5.3 MongoDB 数据库存储
# 条目：5.3.4 插入数据
# 清单：10
# 说明：摘自书稿示例，未改写。

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['spider_db']
collection = db['books']

# 插入一条书籍文档
book = {
    'title': 'Python爬虫实战（第2版）',
    'author': '范传辉',
    'price': 79.00,
    'pub_date': '2025-03-15',
    'tags': ['Python', '爬虫', '实战'],
    'publisher': {
        'name': '机械工业出版社',
        'city': '北京'
    }
}

result = collection.insert_one(book)
print(f"插入成功，文档 ID：{result.inserted_id}")
