# 对应：第11章 爬虫系统的设计
# 小节：11.8 爬虫系统的部署
# 条目：11.8.2 Docker 镜像与 Compose
# 清单：05
# 说明：摘自书稿示例，未改写。

docker compose up -d --build
docker compose ps
docker compose logs -f scheduler
docker compose stop
docker compose start
docker compose down
