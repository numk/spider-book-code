# 对应：第11章 爬虫系统的设计
# 小节：11.6 日志与监控
# 条目：11.6.3 告警通知
# 清单：03
# 说明：摘自书稿示例，未改写。

import time
import requests


class Alerter:
    def __init__(self, webhook="", cooldown=3600, post=requests.post):
        self.webhook, self.cooldown, self.post = webhook, cooldown, post
        self.last_sent = {}

    def notify(self, key, content):
        now = time.monotonic()
        if now - self.last_sent.get(key, float("-inf")) < self.cooldown:
            return False
        if self.webhook:
            response = self.post(self.webhook, json={"msgtype": "text", "text": {"content": content}}, timeout=5)
            response.raise_for_status()
            if response.json().get("errcode") != 0:
                raise RuntimeError("告警服务未确认成功")
        else:
            print("告警预览：{}".format(content))
        self.last_sent[key] = now
        return True


def alert_if_needed(metrics, alerter, min_samples=1, threshold=0.5):
    if metrics.total_requests >= min_samples and metrics.success_rate < threshold:
        alerter.notify("request_failure", f"本轮请求成功率 {metrics.success_rate:.1%}")
