# 对应：第9章 Scrapy 框架的使用
# 小节：9.5 Spider：爬虫编写
# 条目：9.5.1 基础 Spider
# 清单：01
# 说明：摘自书稿示例，未改写。

# spiders/books.py
import scrapy
from book_spider.items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']
    
    def parse(self, response):
        """解析书籍列表页"""
        # 提取本页所有书籍
        for card in response.css('.product_pod'):
            item = BookItem()
            item['title'] = card.css('img::attr(alt)').get()
            item['price'] = card.css('.price_color::text').get(default='').strip()
            
            rating_class = card.css('.star-rating::attr(class)').get(default='')
            item['rating'] = rating_class.split()[-1] if rating_class else ''
            
            # 构造详情页绝对 URL
            relative_url = card.css('h3 a::attr(href)').get()
            item['detail_url'] = response.urljoin(relative_url)
            
            # 跟进详情页获取更多信息
            yield scrapy.Request(
                url=item['detail_url'],
                callback=self.parse_detail,
                meta={'item': item}  # 通过 meta 将 item 传递给详情页解析方法
            )
        
        # 翻页：找到"下一页"链接
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_detail(self, response):
        """解析书籍详情页"""
        item = response.meta['item']
        
        # 提取详情页的额外信息
        item['upc'] = response.css('.table-striped tr:first-child td::text').get(default='')
        item['description'] = response.css('#product_description + p::text').get(default='')
        item['availability'] = response.css('.availability::text').get(default='').strip()
        
        yield item
