# 对应：第4章 数据解析
# 小节：4.2 BeautifulSoup 库的使用
# 条目：4.2.5 CSS 选择器
# 清单：11
# 说明：摘自书稿示例，未改写。

from bs4 import BeautifulSoup

soup = BeautifulSoup(book_list_html, 'lxml')

# 使用 CSS 选择器查找所有书名链接
links = soup.select('ul.book-list li.book-item a.book-link')
for link in links:
    print(link.text, link['href'])

# 查找第一个匹配的元素（等同于 find）
first_link = soup.select_one('a.book-link')
print(first_link.text)
