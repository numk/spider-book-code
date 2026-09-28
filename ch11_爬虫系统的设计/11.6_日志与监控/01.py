# 对应：第11章 爬虫系统的设计
# 小节：11.6 日志与监控
# 条目：11.6.1 结构化日志
# 清单：01
# 说明：摘自书稿示例，未改写。

from pathlib import Path
from loguru import logger

Path("logs").mkdir(exist_ok=True)
logger.add("logs/spider.jsonl", serialize=True, encoding="utf-8", rotation="10 MB", retention="7 days")
logger.bind(task_id="lesson").info("采集开始")
