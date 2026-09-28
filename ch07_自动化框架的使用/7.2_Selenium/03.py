# 对应：第7章 自动化框架的使用
# 小节：7.2 Selenium
# 条目：7.2.3 快速上手
# 清单：03
# 说明：摘自书稿示例，未改写。

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')          # 无头模式，不显示浏览器窗口
options.add_argument('--no-sandbox')        # 在 Docker/Linux 中需要
options.add_argument('--disable-dev-shm-usage')  # 解决内存不足问题

driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')
print(driver.title)
driver.quit()
