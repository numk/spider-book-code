# 对应：第4章 数据解析
# 小节：4.3 XPath 的使用
# 条目：4.3.5 结合 requests 进行实战
# 清单：03
# 说明：摘自书稿示例，未改写。

import requests
from lxml import etree

url = "https://books.toscrape.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

# 将响应文本解析为 lxml 对象
tree = etree.HTML(response.text)

# 获取所有书籍节点
books = tree.xpath('//article[@class="product_pod"]')
print(f"本页共有 {len(books)} 本书")
print("-" * 50)

for book in books:
    # 书名在 img 标签的 alt 属性中
    title = book.xpath('.//img/@alt')[0]
    # 价格
    price = book.xpath('string(.//p[@class="price_color"])').strip()
    # 评级（从 class 属性中提取，如 "star-rating Three"，取第二个值）
    rating_classes = book.xpath('.//p[contains(@class,"star-rating")]/@class')[0]
    rating = rating_classes.split()[-1]
    # 详情链接
    link = book.xpath('.//h3/a/@href')[0]

    print(f"《{title}》  {price}  评级：{rating}  链接：{link}")
