# 对应：第9章 Scrapy 框架的使用
# 小节：9.2 安装与创建项目
# 条目：9.2.2 创建 Scrapy 项目
# 清单：07
# 说明：摘自书稿示例，未改写。

import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        pass
