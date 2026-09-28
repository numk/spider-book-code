# 对应：第11章 爬虫系统的设计
# 小节：11.9 登录态管理与 Cookie 池
# 条目：11.9.1 为什么需要 Cookie 池
# 清单：02
# 说明：摘自书稿示例，未改写。

import redis
import json

r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)

def save_cookies_to_redis(account: str, cookies: dict):
    key = f'cookie:{account}'
    r.set(key, json.dumps(cookies))
    r.expire(key, 86400 * 7)   # 7 天过期
    print(f'已保存 {account} 的 Cookie 到 Redis')

def load_cookies_from_redis(account: str) -> dict | None:
    key = f'cookie:{account}'
    raw = r.get(key)
    return json.loads(raw) if raw else None
