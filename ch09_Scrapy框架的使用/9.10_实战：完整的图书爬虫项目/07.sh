# 对应：第9章 Scrapy 框架的使用
# 小节：9.10 实战：完整的图书爬虫项目
# 条目：运行爬虫
# 清单：07
# 说明：摘自书稿示例，未改写。

# 进入项目目录
cd book_spider

# 运行爬虫（数据存入 MySQL）
scrapy crawl books_full

# 或者同时导出到 JSON 文件
scrapy crawl books_full -o books_full.json
