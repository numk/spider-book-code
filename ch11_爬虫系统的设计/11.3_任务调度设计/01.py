# 对应：第11章 爬虫系统的设计
# 小节：11.3 任务调度设计
# 条目：11.3.2 使用 APScheduler 实现定时调度
# 清单：01
# 说明：摘自书稿示例，未改写。

from datetime import datetime, timedelta, timezone
from apscheduler.schedulers.blocking import BlockingScheduler

def lesson_job(label):
    print("触发 {}".format(label))

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(lesson_job, "cron", hour=8, args=["每日"], id="daily")
    scheduler.add_job(lesson_job, "interval", minutes=30, args=["间隔"], id="interval")
    scheduler.add_job(lesson_job, "date", run_date=datetime.now(timezone.utc) + timedelta(seconds=10),
                      args=["单次"], id="once")
    scheduler.start()
