# 对应：第14章 爬虫与法律
# 小节：14.5 合规爬虫的实践指南
# 条目：14.5.2 采集中的工程控制
# 清单：01
# 说明：摘自书稿示例，未改写。

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS = 4
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_TIMEOUT = 30
USER_AGENT = 'ResearchBot/1.0 (+https://example.com/bot-info)'
