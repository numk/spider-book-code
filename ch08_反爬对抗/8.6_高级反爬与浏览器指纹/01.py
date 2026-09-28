# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.1 浏览器指纹检测
# 清单：01
# 说明：摘自书稿示例，未改写。

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

# 执行 JS 覆盖 webdriver 属性
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    '''
})

driver.get('https://bot.sannysoft.com/')  # 这个网站可以检测自动化特征
