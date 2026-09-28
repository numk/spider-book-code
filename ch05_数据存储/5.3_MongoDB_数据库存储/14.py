# 对应：第5章 数据存储
# 小节：5.3 MongoDB 数据库存储
# 条目：5.3.6 更新数据
# 清单：14
# 说明：摘自书稿示例，未改写。

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
collection = client['spider_db']['books']

# 更新单条文档
result = collection.update_one(
    {'title': 'Python爬虫实战（第2版）'},  # 查询条件
    {'$set': {'price': 69.00, 'discount': True}}  # 更新内容
)
print(f"匹配文档数：{result.matched_count}，更新文档数：{result.modified_count}")

# 更新多条文档：给所有价格超过 80 元的书籍添加 "精品" 标签
result = collection.update_many(
    {'price': {'$gt': 80}},
    {'$set': {'is_premium': True}}
)
print(f"批量更新完成，影响 {result.modified_count} 条文档")
