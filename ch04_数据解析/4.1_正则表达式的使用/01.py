# 对应：第4章 数据解析
# 小节：4.1 正则表达式的使用
# 条目：4.1.3 re 模块的常用方法
# 清单：01
# 说明：摘自书稿示例，未改写。

import re

html = """
<ul>
    <li class="item"><a href="/book/1">Python爬虫实战</a></li>
    <li class="item"><a href="/book/2">Python数据分析</a></li>
    <li class="item"><a href="/book/3">Python机器学习</a></li>
</ul>
"""

# 提取所有书名
titles = re.findall(r'<a href=".*?">(.*?)</a>', html)
print(titles)
