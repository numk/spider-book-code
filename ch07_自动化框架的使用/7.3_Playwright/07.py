# 对应：第7章 自动化框架的使用
# 小节：7.3 Playwright
# 条目：7.3.6 网络请求拦截
# 清单：07
# 说明：摘自书稿示例，未改写。

from playwright.sync_api import sync_playwright

def handle_request(route, request):
    """请求拦截处理器"""
    # 屏蔽图片和字体请求，加快页面加载速度（爬虫场景非常实用）
    if request.resource_type in ['image', 'font', 'stylesheet']:
        route.abort()
    else:
        route.continue_()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # 注册请求拦截器
    page.route('**/*', handle_request)
    
    import time
    start = time.time()
    page.goto('https://www.baidu.com')
    page.wait_for_load_state('domcontentloaded')
    print(f"加载耗时（拦截图片/字体/CSS）：{time.time() - start:.2f} 秒")
    print(f"页面标题：{page.title()}")
    
    browser.close()
