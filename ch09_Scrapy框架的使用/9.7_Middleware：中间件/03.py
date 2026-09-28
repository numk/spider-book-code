# 对应：第9章 Scrapy 框架的使用
# 小节：9.7 Middleware：中间件
# 条目：9.7.3 请求重试中间件
# 清单：03
# 说明：摘自书稿示例，未改写。

# settings.py
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
RETRY_ENABLED = True
RETRY_TIMES = 3          # 最大重试次数
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]  # 触发重试的状态码
