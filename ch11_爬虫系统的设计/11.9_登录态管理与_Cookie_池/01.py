# 对应：第11章 爬虫系统的设计
# 小节：11.9 登录态管理与 Cookie 池
# 条目：11.9.1 为什么需要 Cookie 池
# 清单：01
# 说明：摘自书稿示例，未改写。

from pathlib import Path
import requests
import json

def login(username: str, password: str) -> requests.Session:
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    })

    # 第一步：获取登录页面（有些站点需要先拿 CSRF token）
    resp = session.get('https://www.example.com/login')

    # 第二步：提交登录表单
    payload = {
        'username': username,
        'password': password,
        # 'csrf_token': parse_csrf(resp.text),  # 如果有 CSRF token
    }
    resp = session.post('https://www.example.com/api/login', json=payload)
    resp.raise_for_status()

    data = resp.json()
    if data.get('code') != 0:
        raise ValueError(f'登录失败: {data.get("msg")}')

    return session

def save_cookies(session: requests.Session, filepath: str):
    """将 Session 的 Cookie 序列化保存到文件"""
    cookies = {c.name: c.value for c in session.cookies}
    with Path(filepath).open('w', encoding='utf-8') as f:
        json.dump(cookies, f, ensure_ascii=False, indent=2)
    print(f'Cookie 已保存: {filepath}')

def load_cookies(filepath: str) -> dict:
    """从文件加载 Cookie"""
    with Path(filepath).open(encoding='utf-8') as f:
        return json.load(f)

# 使用示例
session = login('user@example.com', 'password123')
save_cookies(session, 'cookies_user1.json')

# 后续请求直接用这个 session
resp = session.get('https://www.example.com/api/profile')
print(resp.json())
