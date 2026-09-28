# 对应：第9章 Scrapy 框架的使用
# 小节：9.9 Scrapy 的常用命令
# 条目：9.8.1 通过命令行导出数据
# 清单：01
# 说明：摘自书稿示例，未改写。

# 创建项目
scrapy startproject <项目名>

# 创建爬虫
scrapy genspider <爬虫名> <域名>
scrapy genspider -t crawl <爬虫名> <域名>  # 创建 CrawlSpider 类型

# 运行爬虫
scrapy crawl <爬虫名>
scrapy crawl <爬虫名> -o output.json       # 运行并导出到文件
scrapy crawl <爬虫名> -s LOG_LEVEL=WARNING # 临时覆盖配置

# 交互式调试
scrapy shell "<URL>"                        # 打开 Shell 测试选择器

# 查看项目信息
scrapy list                                 # 列出所有爬虫
scrapy settings --get DOWNLOAD_DELAY        # 查看某项配置的值

# 检查爬虫
scrapy check <爬虫名>                       # 检查爬虫是否有错误
