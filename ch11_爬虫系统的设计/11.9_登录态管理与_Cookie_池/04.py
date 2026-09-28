# 对应：第11章 爬虫系统的设计
# 小节：11.9 登录态管理与 Cookie 池
# 条目：11.9.4 适配与初始化
# 清单：04
# 说明：摘自书稿示例，未改写。

import redis
from cookies import CookiePool, fetch_with_cookie

def classify(response):
    # 仅用于约定返回 authenticated 字段的教学接口。
    if response.status_code == 401:
        return "invalid"
    if response.status_code != 200:
        return "unknown"
    try:
        data = response.json()
    except ValueError:
        return "unknown"
    if data.get("authenticated") is True:
        return "valid"
    if data.get("error") == "SESSION_EXPIRED":
        return "invalid"
    return "unknown"
