# 对应：第9章 Scrapy 框架的使用
# 小节：9.4 Item：定义数据结构
# 条目：9.2.2 创建 Scrapy 项目
# 清单：02
# 说明：摘自书稿示例，未改写。

from book_spider.items import BookItem

def parse(self, response):
    for card in response.css('.product_pod'):
        item = BookItem()
        item['title'] = card.css('img::attr(alt)').get()
        item['price'] = card.css('.price_color::text').get()
        yield item
