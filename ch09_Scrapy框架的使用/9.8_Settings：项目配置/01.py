# 对应：第9章 Scrapy 框架的使用
# 小节：9.8 Settings：项目配置
# 条目：9.7.4 启用中间件
# 清单：01
# 说明：摘自书稿示例，未改写。

# settings.py

# 爬虫名称
BOT_NAME = 'book_spider'

# 爬虫模块路径
SPIDER_MODULES = ['book_spider.spiders']
NEWSPIDER_MODULE = 'book_spider.spiders'

# ====== 礼貌性设置 ======
# 是否遵守 robots.txt（生产环境建议开启）
ROBOTSTXT_OBEY = False

# 相邻两次下载请求之间的延迟（秒）
DOWNLOAD_DELAY = 1

# 自动限速：根据服务器响应时间自动调整速度
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1      # 初始下载延迟
AUTOTHROTTLE_MAX_DELAY = 10       # 最大下载延迟
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0  # 目标并发请求数

# ====== 并发控制 ======
CONCURRENT_REQUESTS = 16                   # 全局最大并发请求数
CONCURRENT_REQUESTS_PER_DOMAIN = 8        # 对同一域名的最大并发请求数
CONCURRENT_REQUESTS_PER_IP = 0            # 对同一 IP 的最大并发（0 表示不限制）

# ====== 请求设置 ======
DOWNLOAD_TIMEOUT = 15                      # 请求超时时间（秒）
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

# ====== 重试设置 ======
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# ====== 数据库配置 ======
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DATABASE = 'spider_db'

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'spider_db'

# ====== 日志设置 ======
LOG_LEVEL = 'INFO'   # 日志级别：DEBUG/INFO/WARNING/ERROR
# LOG_FILE = 'scrapy.log'  # 将日志输出到文件

# ====== 数据导出 ======
# 可以通过命令行参数覆盖：scrapy crawl books -o output.json
FEED_EXPORT_ENCODING = 'utf-8'
