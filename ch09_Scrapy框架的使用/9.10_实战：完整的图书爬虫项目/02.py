# 对应：第9章 Scrapy 框架的使用
# 小节：9.10 实战：完整的图书爬虫项目
# 条目：items.py
# 清单：02
# 说明：摘自书稿示例，未改写。

import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    availability = scrapy.Field()
    upc = scrapy.Field()
    description = scrapy.Field()
    detail_url = scrapy.Field()
    num_reviews = scrapy.Field()
