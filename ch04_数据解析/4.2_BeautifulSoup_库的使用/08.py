# 对应：第4章 数据解析
# 小节：4.2 BeautifulSoup 库的使用
# 条目：4.2.4 查找元素
# 清单：08
# 说明：摘自书稿示例，未改写。

from bs4 import BeautifulSoup

soup = BeautifulSoup(book_list_html, 'lxml')

# 查找所有 li 标签
all_items = soup.find_all('li', class_='book-item')
print(f"共找到 {len(all_items)} 本书")

for item in all_items:
    # 提取书名
    title = item.find('a', class_='book-link').text
    # 提取价格
    price = item.find('span', class_='price').text
    # 提取链接
    link = item.find('a')['href']
    print(f"书名：{title}，价格：{price}，链接：{link}")
