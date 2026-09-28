# 对应：第9章 Scrapy 框架的使用
# 小节：9.10 实战：完整的图书爬虫项目
# 条目：middlewares.py
# 清单：05
# 说明：摘自书稿示例，未改写。

import random

class RandomUserAgentMiddleware:
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    ]
    
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.USER_AGENTS)
