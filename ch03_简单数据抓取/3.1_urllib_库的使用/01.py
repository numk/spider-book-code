# 对应：第3章 简单数据抓取
# 小节：3.1 urllib 库的使用
# 条目：3.1.2 urllib 库的使用
# 清单：01
# 说明：摘自书稿示例，未改写。

import urllib.request

url = "http://example.com"
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")
print(html)
