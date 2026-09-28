# 对应：第2章 爬虫软件的安装
# 小节：2.5 Docker：容器化开发与部署
# 条目：2.5.4 Docker 的基本使用
# 清单：07
# 说明：摘自书稿示例，未改写。

# 交互模式运行容器，进入容器命令行
docker run -it --name my-python python:3.12-slim bash

# 后台运行 Redis（-d 后台，-p 端口映射）
docker run -d --name my-redis -p 6379:6379 redis:7

# 后台运行 MongoDB，并挂载数据目录到宿主机（数据持久化）
docker run -d --name my-mongo \
  -p 27017:27017 \
  -v /data/mongo:/data/db \
  mongo:7
