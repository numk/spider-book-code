# 对应：第4章 数据解析
# 小节：4.2 BeautifulSoup 库的使用
# 条目：4.2.4 查找元素
# 清单：06
# 说明：摘自书稿示例，未改写。

# 通过 id 查找
title = soup.find('h1', id='main-title')
print(title.text)

# 通过 class 查找（注意：class 是 Python 保留字，需要用下划线 class_）
container = soup.find('div', class_='container')
print(container)
