# 对应：第5章 数据存储
# 小节：5.3 MongoDB 数据库存储
# 条目：5.3.7 删除数据
# 清单：15
# 说明：摘自书稿示例，未改写。

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
collection = client['spider_db']['books']

# 删除单条文档
result = collection.delete_one({'title': 'Python机器学习'})
print(f"删除了 {result.deleted_count} 条文档")

# 删除多条文档：删除所有价格低于 60 元的书籍
result = collection.delete_many({'price': {'$lt': 60}})
print(f"批量删除了 {result.deleted_count} 条文档")
