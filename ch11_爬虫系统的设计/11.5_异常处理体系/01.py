# 对应：第11章 爬虫系统的设计
# 小节：11.5 异常处理体系
# 条目：11.5.2 统一异常处理框架
# 清单：01
# 说明：摘自书稿示例，未改写。

import time
import requests
from functools import wraps
from typing import Optional



def with_retry(max_retries: int = 3, base_delay: float = 1.0, exceptions=(Exception,)):
    """通用重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries:
                        print(f"{func.__name__} 最终失败: {e}")
                        raise
                    delay = base_delay * (2 ** attempt)
                    print(f"{func.__name__} 第 {attempt + 1} 次失败: {e}，{delay:.1f}s 后重试")
                    time.sleep(delay)
        return wrapper
    return decorator


@with_retry(max_retries=3, exceptions=(requests.RequestException,))
def fetch(url: str, **kwargs) -> requests.Response:
    response = requests.get(url, timeout=10, **kwargs)
    response.raise_for_status()
    return response


def safe_parse(html: str, parser_func, url: str = "") -> Optional[dict]:
    """安全解析：失败时输出错误并返回 None，不抛出异常"""
    try:
        return parser_func(html)
    except Exception as e:
        print(f"解析失败 [{url}]: {e}")
        return None
