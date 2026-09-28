# 对应：第4章 数据解析
# 小节：4.2 BeautifulSoup 库的使用
# 条目：4.2.6 实战：用 BeautifulSoup 爬取 Books to Scrape 图书数据
# 清单：13
# 说明：摘自书稿示例，未改写。

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

# 找到所有书籍条目
books = soup.find_all('article', class_='product_pod')

print(f"本页共有 {len(books)} 本书")
print("-" * 50)

for book in books:
    # 提取书名（书名存放在 img 标签的 alt 属性中）
    title = book.find('img')['alt']
    # 提取价格
    price = book.find('p', class_='price_color').text.strip()
    # 提取评级（星级存放在 p 标签的 class 属性中，如 "star-rating Three"）
    rating_class = book.find('p', class_='star-rating')['class']
    rating = rating_class[1]  # 取第二个 class 名，如 "Three"
    # 提取详情链接
    link = book.find('a')['href']

    print(f"书名：{title}")
    print(f"价格：{price}  评级：{rating}  链接：{link}")
    print()
