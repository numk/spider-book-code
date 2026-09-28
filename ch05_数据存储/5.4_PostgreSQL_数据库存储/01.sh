# 对应：第5章 数据存储
# 小节：5.4 PostgreSQL 数据库存储
# 条目：5.4.2 安装 PostgreSQL 和驱动库
# 清单：01
# 说明：摘自书稿示例，未改写。

docker run --name my-postgres -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=root -e POSTGRES_DB=spider_db -d -p 5432:5432 postgres:latest
