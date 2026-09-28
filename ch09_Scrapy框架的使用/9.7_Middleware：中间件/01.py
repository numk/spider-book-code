# 对应：第9章 Scrapy 框架的使用
# 小节：9.7 Middleware：中间件
# 条目：9.7.1 随机 User-Agent 中间件
# 清单：01
# 说明：摘自书稿示例，未改写。

# middlewares.py
import random

class RandomUserAgentMiddleware:
    """随机 User-Agent 中间件"""
    
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    ]
    
    def process_request(self, request, spider):
        """在每个 Request 发出前，随机替换 User-Agent"""
        request.headers['User-Agent'] = random.choice(self.USER_AGENTS)
        return None  # 返回 None 表示继续正常处理，不拦截
