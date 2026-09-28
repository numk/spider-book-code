# 对应：第3章 简单数据抓取
# 小节：3.2 requests 库的使用
# 条目：3.2.8 超时与异常处理
# 清单：16
# 说明：摘自书稿示例，未改写。

import requests

url = "https://httpbin.org/delay/2"

try:
    response = requests.get(url, timeout=3)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.HTTPError as e:
    print("HTTP 错误：", e)
except requests.exceptions.RequestException as e:
    print("请求失败：", e)
