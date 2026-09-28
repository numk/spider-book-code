# 对应：第11章 爬虫系统的设计
# 小节：11.9 登录态管理与 Cookie 池
# 条目：11.9.3 Cookie 池与任务账号
# 清单：03
# 说明：摘自书稿示例，未改写。

"""Inject site-specific login/validation; never infer expiry from every 403."""
import json
import random
import time
from threading import Thread, Event
import requests
import traceback


class CookiePool:
    def __init__(self, client, refresh, validate, max_refresh=2):
        self.r, self.refresh, self.validate = client, refresh, validate
        self.max_refresh = max_refresh
        self.pool_key, self.invalid_key = "cookie_pool", "cookie_invalid"
        self.stop = Event()

    def add(self, account, cookies):
        with self.r.pipeline(transaction=True) as pipe:
            pipe.hset(self.pool_key, account, json.dumps(cookies))
            pipe.srem(self.invalid_key, account)
            pipe.execute()

    def get_by_account(self, account):
        raw = self.r.hget(self.pool_key, account)
        return json.loads(raw) if raw else None

    def get(self):
        accounts = self.all_accounts()
        if not accounts:
            return None
        account = random.choice(accounts)
        cookies = self.get_by_account(account)
        return (account, cookies) if cookies is not None else None

    def mark_invalid(self, account):
        with self.r.pipeline(transaction=True) as pipe:
            pipe.hdel(self.pool_key, account)
            pipe.sadd(self.invalid_key, account)
            pipe.execute()

    def size(self):
        return self.r.hlen(self.pool_key)

    def all_accounts(self):
        return self.r.hkeys(self.pool_key)

    def invalid_accounts(self):
        return list(self.r.smembers(self.invalid_key))

    def refresh_account(self, account):
        self.mark_invalid(account)
        for attempt in range(self.max_refresh):
            try:
                cookies = self.refresh(account)
                if cookies and self.validate(cookies) == "valid":
                    self.add(account, cookies)
                    return cookies
            except requests.RequestException:
                print("刷新暂时失败，尝试 {}".format(attempt + 1))
        print("账号已暂停，需要人工检查")
        return None

    def health_check(self):
        for account in self.all_accounts():
            cookies = self.get_by_account(account)
            if cookies is None:
                continue
            try:
                state = self.validate(cookies)
            except requests.RequestException:
                state = "unknown"
            if state == "invalid":
                self.refresh_account(account)
            elif state == "unknown":
                print("校验暂不可用，保留现有 Cookie")

    def start_health_check_loop(self, interval=1800):
        def loop():
            while not self.stop.is_set():
                try:
                    self.health_check()
                except Exception:
                    print("健康检查异常", traceback.format_exc())
                self.stop.wait(interval)
        thread = Thread(target=loop, daemon=True)
        thread.start()
        return thread


def fetch_with_cookie(pool, account, url, classify, get=requests.get, max_attempts=3):
    """account is fixed for the whole task, including pagination and retries."""
    refreshed = False
    for attempt in range(max_attempts):
        cookies = pool.get_by_account(account)
        if cookies is None:
            raise RuntimeError("账号不可用，暂停当前任务")
        try:
            response = get(url, cookies=cookies, timeout=10, allow_redirects=False)
            state = classify(response)
            if state == "invalid":
                if refreshed:
                    pool.mark_invalid(account)
                    raise RuntimeError("刷新后仍失效，暂停账号")
                refreshed = True
                if pool.refresh_account(account) is None:
                    raise RuntimeError("刷新失败，暂停当前任务")
                continue
            if state == "unknown":
                raise requests.RequestException("临时网络、限流或未识别响应")
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            if attempt + 1 == max_attempts:
                raise
            time.sleep(min(2 ** attempt, 4))
    raise RuntimeError("请求次数达到上限")
