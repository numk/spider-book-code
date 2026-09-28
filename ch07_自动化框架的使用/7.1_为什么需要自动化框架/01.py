# 对应：第7章 自动化框架的使用
# 小节：7.1 为什么需要自动化框架
# 清单：01
# 说明：摘自书稿示例，未改写。

import requests
from lxml import etree

url = 'https://spa1.scrape.center/'  # 这是一个纯 JS 渲染的练习网站
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(url, headers=headers)
tree = etree.HTML(response.text)

# 尝试提取电影标题
titles = tree.xpath('//h2[@class]/text()')
print(f"找到 {len(titles)} 个标题")
print(response.text[:500])
