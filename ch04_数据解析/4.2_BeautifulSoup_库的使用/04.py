# 对应：第4章 数据解析
# 小节：4.2 BeautifulSoup 库的使用
# 条目：4.2.4 查找元素
# 清单：04
# 说明：摘自书稿示例，未改写。

from bs4 import BeautifulSoup

soup = BeautifulSoup(book_list_html, 'lxml')

# 查找第一个 li 标签
first_item = soup.find('li')
print(first_item)
