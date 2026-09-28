# 对应：第9章 Scrapy 框架的使用
# 小节：9.4 Item：定义数据结构
# 条目：9.2.2 创建 Scrapy 项目
# 清单：03
# 说明：摘自书稿示例，未改写。

def parse(self, response):
    for card in response.css('.product_pod'):
        yield {
            'title': card.css('img::attr(alt)').get(),
            'price': card.css('.price_color::text').get(),
        }
