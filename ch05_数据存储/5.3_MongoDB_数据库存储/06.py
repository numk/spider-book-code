# 对应：第5章 数据存储
# 小节：5.3 MongoDB 数据库存储
# 条目：5.3.3 连接 MongoDB
# 清单：06
# 说明：摘自书稿示例，未改写。

import pymongo

# 连接到本地 MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')

# 选择数据库（如果不存在会自动创建）
db = client['spider_db']

# 选择集合（如果不存在会自动创建）
collection = db['books']

print("连接成功！")
