# 对应：第2章 爬虫软件的安装
# 小节：2.5 Docker：容器化开发与部署
# 条目：2.5.4 Docker 的基本使用
# 清单：08
# 说明：摘自书稿示例，未改写。

# 查看正在运行的容器
docker ps

# 查看所有容器（包括已停止的）
docker ps -a

# 停止 / 启动 / 重启容器
docker stop my-redis
docker start my-redis
docker restart my-redis

# 删除容器（需先停止）
docker rm my-redis

# 进入正在运行的容器执行命令
docker exec -it my-redis bash

# 查看容器日志（-f 实时跟踪）
docker logs -f my-python

# 查看本地所有镜像
docker images

# 删除镜像
docker rmi python:3.12-slim

# 查看容器资源占用
docker stats
