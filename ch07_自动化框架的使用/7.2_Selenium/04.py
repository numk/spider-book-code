# 对应：第7章 自动化框架的使用
# 小节：7.2 Selenium
# 条目：7.2.4 元素定位
# 清单：04
# 说明：摘自书稿示例，未改写。

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 通过 ID 定位（最快最准确）
search_box = driver.find_element(By.ID, 'kw')

# 通过 NAME 属性定位
search_box = driver.find_element(By.NAME, 'wd')

# 通过 CSS 选择器定位（灵活、推荐）
search_box = driver.find_element(By.CSS_SELECTOR, 'input#chat-textarea')
search_btn = driver.find_element(By.CSS_SELECTOR, '#chat-submit-button')

# 通过 XPath 定位（功能最强大）
search_box = driver.find_element(By.XPATH, '//*[@id="kw"]')

# 通过文本内容定位（适合找按钮、链接）
link = driver.find_element(By.LINK_TEXT, '新闻')

# 通过 CLASS_NAME 定位
items = driver.find_elements(By.CLASS_NAME, 's_ipt')  # 返回列表

driver.quit()
