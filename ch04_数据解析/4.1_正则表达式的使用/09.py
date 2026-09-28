# 对应：第4章 数据解析
# 小节：4.1 正则表达式的使用
# 条目：4.1.4 实战：逐条提取网页数据
# 清单：09
# 说明：摘自书稿示例，未改写。

book_list_html = """<html><head><title>Python书籍列表</title></head><body>
<div class="container"><h1 id="main-title">热门Python书籍</h1>
<ul class="book-list">
<li class="book-item"><a href="/book/1" class="book-link">Python爬虫实战</a><span class="price">¥79.00</span></li>
<li class="book-item"><a href="/book/2" class="book-link">Python数据分析</a><span class="price">¥59.00</span></li>
</ul></div></body></html>"""
