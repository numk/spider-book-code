# 对应：第9章 Scrapy 框架的使用
# 小节：9.8 Settings：项目配置
# 条目：9.8.1 通过命令行导出数据
# 清单：02
# 说明：摘自书稿示例，未改写。

# 导出为 JSON
scrapy crawl books -o books.json

# 导出为 CSV
scrapy crawl books -o books.csv

# 导出为 JSON Lines（每行一个 JSON 对象，适合大数据量）
scrapy crawl books -o books.jl

# 导出 XML
scrapy crawl books -o books.xml
