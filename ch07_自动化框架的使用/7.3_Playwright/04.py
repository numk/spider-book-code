# 对应：第7章 自动化框架的使用
# 小节：7.3 Playwright
# 条目：7.3.3 同步模式快速上手
# 清单：04
# 说明：摘自书稿示例，未改写。

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # 启动 Chromium 浏览器
    browser = p.chromium.launch(headless=False)  # headless=True 为无头模式
    
    # 创建新页面（Tab）
    page = browser.new_page()
    
    # 打开页面
    page.goto('https://www.baidu.com')
    print(f"页面标题：{page.title()}")
    
    # 查找元素并操作
    page.fill('#kw', 'Playwright 爬虫')  # 填写输入框
    page.click('#su')                   # 点击搜索按钮
    
    # 等待搜索结果加载
    page.wait_for_selector('.result .t')
    
    # 提取搜索结果
    results = page.query_selector_all('.result .t a')
    print(f"\n搜索结果（前3条）：")
    for r in results[:3]:
        print(f"  {r.inner_text()}")
    
    # 截图
    page.screenshot(path='playwright_demo.png')
    
    browser.close()
