# 对应：第9章 Scrapy 框架的使用
# 小节：9.5 Spider：爬虫编写
# 条目：9.5.2 CrawlSpider：自动跟踪链接
# 清单：03
# 说明：摘自书稿示例，未改写。

# spiders/books_crawl.py
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']
    
    rules = (
        # 规则1：提取翻页链接，继续跟进（follow=True），但不解析（没有 callback）
        Rule(LinkExtractor(restrict_css='.next a'), follow=True),
        
        # 规则2：提取书籍详情链接，用 parse_detail 方法解析
        Rule(
            LinkExtractor(restrict_css='.product_pod h3 a'),
            callback='parse_detail'
        ),
    )
    
    def parse_detail(self, response):
        """解析书籍详情页"""
        yield {
            'title': response.css('h1::text').get(),
            'price': response.css('.price_color::text').get(default='').strip(),
            'upc': response.css('.table-striped tr:first-child td::text').get(default=''),
            'description': response.css('#product_description + p::text').get(default=''),
            'availability': response.css('.availability::text').get(default='').strip(),
            'url': response.url,
        }
