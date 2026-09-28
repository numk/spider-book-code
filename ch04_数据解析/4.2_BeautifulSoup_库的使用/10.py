# 对应：第4章 数据解析
# 小节：4.2 BeautifulSoup 库的使用
# 条目：4.2.4 查找元素
# 清单：10
# 说明：摘自书稿示例，未改写。

price_tag = item.find('span', class_='price')
price = price_tag.text if price_tag else ''
