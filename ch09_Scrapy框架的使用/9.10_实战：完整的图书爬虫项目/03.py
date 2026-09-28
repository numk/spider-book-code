# 对应：第9章 Scrapy 框架的使用
# 小节：9.10 实战：完整的图书爬虫项目
# 条目：spiders/books_full.py
# 清单：03
# 说明：摘自书稿示例，未改写。

import scrapy
from book_spider.items import BookItem

class BooksFullSpider(scrapy.Spider):
    name = 'books_full'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']
    
    # 评级文字 → 数字的映射
    RATING_MAP = {
        'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
    }
    
    def parse(self, response):
        """解析列表页，提取书籍链接和翻页"""
        self.logger.info(f"正在解析列表页：{response.url}")
        
        # 跟进每本书的详情页
        for card in response.css('.product_pod'):
            relative_url = card.css('h3 a::attr(href)').get()
            detail_url = response.urljoin(relative_url)
            
            # 在 meta 中携带列表页已有的简略信息，避免详情页没有时用空值
            yield scrapy.Request(
                url=detail_url,
                callback=self.parse_detail,
                meta={
                    'price': card.css('.price_color::text').get(default='').strip(),
                    'rating_class': card.css('.star-rating::attr(class)').get(default=''),
                }
            )
        
        # 翻页
        next_url = response.css('.next a::attr(href)').get()
        if next_url:
            yield response.follow(next_url, callback=self.parse)
    
    def parse_detail(self, response):
        """解析详情页，提取完整书籍信息"""
        item = BookItem()
        
        # 基本信息
        item['title'] = response.css('h1::text').get(default='').strip()
        item['detail_url'] = response.url
        
        # 价格（优先从详情页取，没有则用列表页传来的值）
        price_str = response.css('.price_color::text').get(default='') or response.meta.get('price', '')
        try:
            item['price'] = float(price_str.replace('£', '').replace('Â', '').strip())
        except ValueError:
            item['price'] = 0.0
        
        # 评级
        rating_class = response.css('.star-rating::attr(class)').get(default='') or response.meta.get('rating_class', '')
        rating_word = rating_class.split()[-1] if rating_class else ''
        item['rating'] = self.RATING_MAP.get(rating_word, 0)
        
        # 产品信息表格（UPC、库存、评论数等）
        table_rows = response.css('.table-striped tr')
        table_data = {}
        for row in table_rows:
            key = row.css('th::text').get(default='').strip()
            value = row.css('td::text').get(default='').strip()
            table_data[key] = value
        
        item['upc'] = table_data.get('UPC', '')
        item['availability'] = table_data.get('Availability', '')
        item['num_reviews'] = int(table_data.get('Number of reviews', '0') or '0')
        
        # 书籍简介（可能不存在）
        item['description'] = response.css('#product_description ~ p::text').get(default='').strip()
        
        self.logger.debug(f"解析完成：《{item['title']}》 £{item['price']}")
        yield item
