# 对应：第4章 数据解析
# 小节：4.1 正则表达式的使用
# 条目：4.1.4 实战：逐条提取网页数据
# 清单：10
# 说明：摘自书稿示例，未改写。

import re

for block in re.findall(r'<li class="book-item">(.*?)</li>', book_list_html, re.S):
    link = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
    price = re.search(r'<span class="price">(.*?)</span>', block, re.S)
    if link:
        print("{} {} {}".format(link.group(2), link.group(1), price.group(1) if price else None))
