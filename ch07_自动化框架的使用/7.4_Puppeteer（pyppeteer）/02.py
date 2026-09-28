# 对应：第7章 自动化框架的使用
# 小节：7.4 Puppeteer（pyppeteer）
# 条目：7.4.3 基本使用
# 清单：02
# 说明：摘自书稿示例，未改写。

import asyncio
from pyppeteer import launch

async def main():
    # 启动浏览器
    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox']
    )
    
    # 打开新页面
    page = await browser.newPage()
    
    # 设置 User-Agent
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
    
    # 导航到目标页面
    await page.goto('https://www.baidu.com', {'waitUntil': 'networkidle2'})
    
    print(f"页面标题：{await page.title()}")
    
    # 在输入框中输入文字
    await page.type('#kw', 'pyppeteer爬虫')
    await page.click('#su')
    
    # 等待搜索结果加载
    await page.waitForSelector('.result .t', {'timeout': 10000})
    
    # 执行 JavaScript 提取数据
    titles = await page.evaluate('''() => {
        const elements = document.querySelectorAll('.result .t a');
        return Array.from(elements).map(el => el.innerText);
    }''')
    
    print(f"\n搜索结果（前5条）：")
    for title in titles[:5]:
        print(f"  {title}")
    
    # 截图
    await page.screenshot({'path': 'pyppeteer_demo.png'})
    
    await browser.close()

asyncio.run(main())
