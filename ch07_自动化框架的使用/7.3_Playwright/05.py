# 对应：第7章 自动化框架的使用
# 小节：7.3 Playwright
# 条目：7.3.4 元素定位与操作
# 清单：05
# 说明：摘自书稿示例，未改写。

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://www.baidu.com')
    
    # CSS 选择器（默认方式）
    search_box = page.locator('#kw')
    
    # XPath
    search_box = page.locator('xpath=//*[@id="kw"]')
    
    # 文本内容定位
    link = page.get_by_text('新闻')
    
    # 占位符文本定位
    input_field = page.get_by_placeholder('请输入搜索内容')
    
    # 组合操作
    page.locator('#kw').fill('Python')
    page.locator('#kw').press('Enter')  # 按 Enter 键
    
    # 等待元素
    page.wait_for_selector('.result')
    page.wait_for_load_state('networkidle')  # 等待网络请求静止（无新请求）
    
    # 获取元素文本和属性
    element = page.locator('.result .t a').first
    print(element.inner_text())
    print(element.get_attribute('href'))
    
    # 获取所有匹配元素
    all_links = page.locator('.result .t a').all()
    for link in all_links[:3]:
        print(link.inner_text())
    
    browser.close()
