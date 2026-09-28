# 对应：第7章 自动化框架的使用
# 小节：7.2 Selenium
# 条目：7.2.6 常用操作
# 清单：08
# 说明：摘自书稿示例，未改写。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 输入文字
input_box = driver.find_element(By.ID, 'kw')
input_box.send_keys('Selenium爬虫')

# 清空输入框
input_box.clear()

# 点击元素
btn = driver.find_element(By.ID, 'su')
btn.click()

# 获取元素文本
time.sleep(2)
results = driver.find_elements(By.CSS_SELECTOR, '.result .t a')
for r in results[:3]:
    print(r.text)

# 获取元素属性
link = driver.find_element(By.CSS_SELECTOR, '.result .t a')
href = link.get_attribute('href')
print(f"链接：{href}")

# 执行 JavaScript（当普通操作无效时非常有用）
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 滚动到页面底部
driver.execute_script('arguments[0].click();', btn)  # 用 JS 点击元素

# 截图
driver.save_screenshot('screenshot.png')

# 获取 cookies
cookies = driver.get_cookies()
print(f"Cookies：{cookies[:2]}")

driver.quit()
