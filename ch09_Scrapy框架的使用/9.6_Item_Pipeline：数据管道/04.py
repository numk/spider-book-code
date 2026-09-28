# 对应：第9章 Scrapy 框架的使用
# 小节：9.6 Item Pipeline：数据管道
# 条目：9.6.5 MongoDB 存储 Pipeline
# 清单：04
# 说明：摘自书稿示例，未改写。

import pymongo

class MongoDBPipeline:
    """MongoDB 存储管道"""
    
    def open_spider(self, spider):
        mongo_uri = spider.settings.get('MONGO_URI', 'mongodb://localhost:27017/')
        db_name = spider.settings.get('MONGO_DATABASE', 'spider_db')
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[db_name]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        collection_name = spider.name  # 以爬虫名命名集合
        self.db[collection_name].insert_one(dict(item))
        return item
