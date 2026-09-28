# 对应：第8章 反爬对抗
# 小节：8.2 请求频率控制
# 条目：8.1.2 完善请求头字段
# 清单：01
# 说明：摘自书稿示例，未改写。

import requests
import time

url = 'https://httpbin.org/get'

for i in range(5):
    response = requests.get(url)
    print(f"第 {i+1} 次请求，状态码：{response.status_code}")
    time.sleep(1)  # 每次请求后等待 1 秒
