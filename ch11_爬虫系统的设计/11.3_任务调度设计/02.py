# 对应：第11章 爬虫系统的设计
# 小节：11.3 任务调度设计
# 条目：11.3.3 任务状态管理
# 清单：02
# 说明：摘自书稿示例，未改写。

import pymysql
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"


class TaskManager:
    def __init__(self, db_config: dict):
        self.db_config = db_config

    def _conn(self):
        return pymysql.connect(**self.db_config)

    def create_task(self, task_name: str, params: dict = None) -> int:
        """创建一条任务记录，返回 task_id"""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO crawl_tasks
                       (task_name, params, status, created_at)
                       VALUES (%s, %s, %s, %s)""",
                    (task_name, str(params), TaskStatus.PENDING.value, datetime.now()),
                )
                conn.commit()
                return cur.lastrowid

    def update_status(self, task_id: int, status: TaskStatus, error_msg: str = None):
        """更新任务状态"""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE crawl_tasks
                       SET status=%s, error_msg=%s, updated_at=%s
                       WHERE id=%s""",
                    (status.value, error_msg, datetime.now(), task_id),
                )
                conn.commit()

    def run_task(self, task_name: str, func, params: dict = None):
        """执行任务并自动记录状态"""
        task_id = self.create_task(task_name, params)
        self.update_status(task_id, TaskStatus.RUNNING)
        try:
            func(**(params or {}))
            self.update_status(task_id, TaskStatus.SUCCESS)
        except Exception as e:
            self.update_status(task_id, TaskStatus.FAILED, str(e))
            raise
