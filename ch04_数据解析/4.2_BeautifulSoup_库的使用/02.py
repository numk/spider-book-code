# 对应：第4章 数据解析
# 小节：4.2 BeautifulSoup 库的使用
# 条目：4.2.3 BeautifulSoup 的基本使用
# 清单：02
# 说明：摘自书稿示例，未改写。

from bs4 import BeautifulSoup

soup = BeautifulSoup(book_list_html, 'lxml')
print(type(soup))
