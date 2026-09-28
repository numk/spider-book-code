# 对应：第9章 Scrapy 框架的使用
# 小节：9.7 Middleware：中间件
# 条目：9.7.4 启用中间件
# 清单：04
# 说明：摘自书稿示例，未改写。

# settings.py
DOWNLOADER_MIDDLEWARES = {
    # 禁用 Scrapy 默认的 User-Agent 中间件
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 启用我们自定义的随机 UA 中间件
    'book_spider.middlewares.RandomUserAgentMiddleware': 400,
    # 启用代理中间件
    'book_spider.middlewares.ProxyMiddleware': 350,
}
