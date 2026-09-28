# 对应：第10章 分布式爬虫的设计
# 小节：10.4 基于 scrapy-redis 的分布式爬虫
# 条目：10.4.2 完整工作节点
# 清单：03
# 说明：摘自书稿示例，未改写。

redis-cli lpush books_lesson:start_urls 'https://books.toscrape.com/catalogue/page-1.html'
redis-cli hlen books_lesson:results
redis-cli zcard books_lesson:requests
