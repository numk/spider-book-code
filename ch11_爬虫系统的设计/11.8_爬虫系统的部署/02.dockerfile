# 对应：第11章 爬虫系统的设计
# 小节：11.8 爬虫系统的部署
# 条目：11.8.2 Docker 镜像与 Compose
# 清单：02
# 说明：摘自书稿示例，未改写。

FROM ghcr.io/astral-sh/uv:0.12.13 AS uv
FROM python:3.12-slim
COPY --from=uv /uv /usr/local/bin/uv
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev
COPY . .
CMD ["uv", "run", "--no-sync", "main.py"]
