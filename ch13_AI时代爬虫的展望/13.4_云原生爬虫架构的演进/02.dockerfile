# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.4 云原生爬虫架构的演进
# 条目：13.4.3 容器化爬虫：Docker + Kubernetes
# 清单：02
# 说明：摘自书稿示例，未改写。

# Dockerfile：包含 Python 爬虫和 Chromium 的镜像
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.12.13 /uv /uvx /bin/

WORKDIR /app
# 先在本地 uv init，再 uv add playwright requests beautifulsoup4
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev && \
    uv run --no-sync playwright install --with-deps chromium
COPY spider.py .

CMD ["uv", "run", "--no-sync", "spider.py"]
