# 对应：第4章 数据解析
# 小节：4.3 XPath 的使用
# 条目：4.3.4 在 Python 中使用 XPath
# 清单：02
# 说明：摘自书稿示例，未改写。

from lxml import etree

tree = etree.HTML(book_list_html)
for item in tree.xpath('//li[@class="book-item"]'):
    title = item.xpath('string(.//a)')
    links = item.xpath('.//a/@href')
    price = item.xpath('string(.//span[@class="price"])')
    print("{} {} {}".format(title, links[0] if links else None, price or None))
