# 对应：第11章 爬虫系统的设计
# 小节：11.7 系统设计实例：图书价格监控
# 条目：11.7.2 运行准备
# 清单：01
# 说明：摘自书稿示例，未改写。

uv init --python 3.12
uv add requests beautifulsoup4 pymysql 'apscheduler>=3.11,<4'
export MYSQL_HOST=localhost
export MYSQL_DATABASE=spider_data
export MYSQL_USER=spider
export MYSQL_PASSWORD='替换为本地数据库密码'
uv run main.py --once
