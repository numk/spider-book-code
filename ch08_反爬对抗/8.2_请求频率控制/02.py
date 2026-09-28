# 对应：第8章 反爬对抗
# 小节：8.2 请求频率控制
# 条目：8.1.2 完善请求头字段
# 清单：02
# 说明：摘自书稿示例，未改写。

import requests
import time
import random

url = 'https://httpbin.org/get'

for i in range(5):
    response = requests.get(url)
    print(f"第 {i+1} 次请求，状态码：{response.status_code}")
    # 随机等待 1~3 秒，更接近真实用户行为
    delay = random.uniform(1.0, 3.0)
    print(f"  等待 {delay:.2f} 秒...")
    time.sleep(delay)
