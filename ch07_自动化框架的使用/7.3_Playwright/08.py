# 对应：第7章 自动化框架的使用
# 小节：7.3 Playwright
# 条目：7.3.6 网络请求拦截
# 清单：08
# 说明：摘自书稿示例，未改写。

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://127.0.0.1:8765")
    with page.expect_response("**/api/search?*") as pending:
        page.get_by_role("button").click()
    response = pending.value
    print("{} {}".format(response.status, response.json()))
    browser.close()
