# 对应：第9章 Scrapy 框架的使用
# 小节：9.4 Item：定义数据结构
# 条目：9.2.2 创建 Scrapy 项目
# 清单：01
# 说明：摘自书稿示例，未改写。

import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()       # 书名
    price = scrapy.Field()       # 价格
    rating = scrapy.Field()      # 评级
    availability = scrapy.Field()  # 库存状态
    detail_url = scrapy.Field()  # 详情页链接
    upc = scrapy.Field()         # 商品编码
    description = scrapy.Field() # 书籍简介
