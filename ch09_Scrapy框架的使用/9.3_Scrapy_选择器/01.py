# 对应：第9章 Scrapy 框架的使用
# 小节：9.3 Scrapy 选择器
# 条目：9.2.2 创建 Scrapy 项目
# 清单：01
# 说明：摘自书稿示例，未改写。

def parse(self, response):
    # ===== CSS 选择器 =====
    # 提取元素文本
    title = response.css('h1.page-title::text').get()
    
    # 提取元素属性
    link = response.css('a.book-link::attr(href)').get()
    
    # 提取所有匹配元素（返回列表）
    all_titles = response.css('.product_pod img::attr(alt)').getall()
    
    # ===== XPath 选择器 =====
    title = response.xpath('//h1[@class="page-title"]/text()').get()
    link = response.xpath('//a[@class="book-link"]/@href').get()
    
    # ===== 链式调用 =====
    # 先定位父节点，再在父节点内提取子节点
    for card in response.css('.product_pod'):
        title = card.css('img::attr(alt)').get()
        price = card.css('.price_color::text').get()
