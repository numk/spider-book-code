# 对应：第7章 自动化框架的使用
# 小节：7.5 DrissionPage
# 条目：7.5.4 SessionPage 模式（纯 HTTP 请求）
# 清单：02
# 说明：摘自书稿示例，未改写。

from DrissionPage import SessionPage

# 创建 SessionPage 对象（纯 HTTP，不需要浏览器）
page = SessionPage()

# 设置请求头
page.set.headers({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# 发送 GET 请求
page.get('https://books.toscrape.com/')

# 提取数据（用法与浏览器模式完全一样！）
books = page.eles('.product_pod')
print(f"获取到 {len(books)} 本书：")

for book in books[:5]:
    title = book.ele('img').attr('alt')
    price = book.ele('.price_color').text
    print(f"  《{title}》  {price}")
