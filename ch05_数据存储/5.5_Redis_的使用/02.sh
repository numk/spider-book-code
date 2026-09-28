# 对应：第5章 数据存储
# 小节：5.5 Redis 的使用
# 条目：5.5.2 安装 Redis 和 Python 驱动
# 清单：02
# 说明：摘自书稿示例，未改写。

docker run --name my-redis -d -p 6379:6379 redis:latest redis-server --requirepass your_password
