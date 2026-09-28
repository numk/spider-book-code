# 对应：第9章 Scrapy 框架的使用
# 小节：9.4 Item：定义数据结构
# 条目：9.4.1 ItemLoader：更优雅的数据填充
# 清单：04
# 说明：摘自书稿示例，未改写。

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()

class BookLoader(ItemLoader):
    default_item_class = BookItem
    
    # TakeFirst：取列表中的第一个值
    # MapCompose：对每个值依次应用函数
    # str.strip：去除首尾空格
    title_out = TakeFirst()
    price_out = MapCompose(str.strip, lambda x: float(x.replace('£', '').replace('Â', '')))
    rating_out = TakeFirst()

# 在 parse 方法中使用 ItemLoader
def parse(self, response):
    for card in response.css('.product_pod'):
        loader = BookLoader(selector=card)
        loader.add_css('title', 'img::attr(alt)')
        loader.add_css('price', '.price_color::text')
        loader.add_css('rating', '.star-rating::attr(class)')
        yield loader.load_item()
