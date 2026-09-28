# 对应：第9章 Scrapy 框架的使用
# 小节：9.6 Item Pipeline：数据管道
# 条目：9.6.6 启用 Pipeline
# 清单：05
# 说明：摘自书稿示例，未改写。

# settings.py
ITEM_PIPELINES = {
    'book_spider.pipelines.CleanPipeline': 100,       # 第1步：清洗数据
    'book_spider.pipelines.DuplicatesPipeline': 200,  # 第2步：去重
    # 'book_spider.pipelines.MySQLPipeline': 400,     # 可选：保存到 MySQL
    # 'book_spider.pipelines.MongoDBPipeline': 400,   # 可选：保存到 MongoDB
}
