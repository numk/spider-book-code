# 对应：第3章 简单数据抓取
# 小节：3.3 httpx 库的使用
# 条目：3.3.2 同步用法
# 清单：04
# 说明：摘自书稿示例，未改写。

import httpx

url = 'https://www.python.org/static/img/python-logo.png'

with httpx.Client() as client:
    with client.stream('GET', url) as response:
        with open('python-logo.png', 'wb') as f:
            for chunk in response.iter_bytes(chunk_size=8192):
                f.write(chunk)

print('下载完成')
