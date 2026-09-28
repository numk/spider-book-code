# 对应：第9章 Scrapy 框架的使用
# 小节：9.10 实战：完整的图书爬虫项目
# 条目：settings.py（关键配置）
# 清单：06
# 说明：摘自书稿示例，未改写。

BOT_NAME = 'book_spider'
SPIDER_MODULES = ['book_spider.spiders']
NEWSPIDER_MODULE = 'book_spider.spiders'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 4

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_TARGET_CONCURRENCY = 4

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'book_spider.middlewares.RandomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
    'book_spider.pipelines.CleanAndValidatePipeline': 100,
    'book_spider.pipelines.MySQLPipeline': 300,
}

# MySQL 配置
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DATABASE = 'spider_db'

LOG_LEVEL = 'INFO'
FEED_EXPORT_ENCODING = 'utf-8'
