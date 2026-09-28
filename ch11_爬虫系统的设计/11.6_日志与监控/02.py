# 对应：第11章 爬虫系统的设计
# 小节：11.6 日志与监控
# 条目：11.6.2 关键指标采集
# 清单：02
# 说明：摘自书稿示例，未改写。

from dataclasses import dataclass, field
from threading import Lock
import time


@dataclass
class SpiderMetrics:
    total_requests: int = 0
    success_requests: int = 0
    failed_requests: int = 0
    total_items: int = 0
    start_time: float = field(default_factory=time.monotonic)
    _lock: Lock = field(default_factory=Lock, repr=False)

    def record_request(self, success):
        with self._lock:
            self.total_requests += 1
            self.success_requests += int(success)
            self.failed_requests += int(not success)

    def record_item(self, count=1):
        with self._lock:
            self.total_items += count

    @property
    def success_rate(self):
        with self._lock:
            return self.success_requests / self.total_requests if self.total_requests else 0.0

    def summary(self):
        with self._lock:
            elapsed = max(time.monotonic() - self.start_time, 0.000001)
            return dict(total_requests=self.total_requests, success_requests=self.success_requests,
                        failed_requests=self.failed_requests, total_items=self.total_items,
                        elapsed_seconds=elapsed, requests_per_second=self.total_requests / elapsed)
