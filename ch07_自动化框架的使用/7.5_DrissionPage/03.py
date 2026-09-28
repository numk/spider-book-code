# 对应：第7章 自动化框架的使用
# 小节：7.5 DrissionPage
# 条目：7.5.5 双模式无缝切换
# 清单：03
# 说明：摘自书稿示例，未改写。

from DrissionPage import WebPage

# WebPage 同时支持浏览器模式和 HTTP 模式
page = WebPage()

# 第一步：用浏览器模式（d 模式）登录，获取 Cookie
page.change_mode('d')  # 切换到浏览器模式
page.get('https://example.com/login')

page.ele('@name=username').input('your_username')
page.ele('@name=password').input('your_password')
page.ele('@type=submit').click()

page.wait.load_start()
print("登录成功！")
print(f"当前 Cookie：{page.cookies()}")

# 第二步：切换到 HTTP 模式（s 模式），复用 Cookie，高速爬取
page.change_mode('s')  # 切换到 HTTP 模式，Cookie 自动携带

# 此时是纯 HTTP 请求，速度极快，且已经携带了登录状态
page.get('https://example.com/data')
data = page.eles('.data-item')
print(f"获取到 {len(data)} 条数据")

page.quit()
