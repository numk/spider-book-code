# 对应：第2章 爬虫软件的安装
# 小节：2.5 Docker：容器化开发与部署
# 条目：2.5.4 Docker 的基本使用
# 清单：06
# 说明：摘自书稿示例，未改写。

# 从 Docker Hub 拉取 Python 官方镜像（slim 版本体积较小，适合爬虫）
docker pull python:3.12-slim

# 拉取 Redis
docker pull redis:7

# 拉取 MongoDB
docker pull mongo:7
