# 对应：第4章 数据解析
# 小节：4.1 正则表达式的使用
# 条目：4.1.3 re 模块的常用方法
# 清单：07
# 说明：摘自书稿示例，未改写。

import re

pattern = re.compile(r'<span class="price">(.*?)</span>')

html_list = [
    '<span class="price">¥49.00</span>',
    '<span class="price">¥68.00</span>',
    '<span class="price">¥99.00</span>',
]

for html in html_list:
    match = pattern.search(html)
    if match:
        print(match.group(1))
