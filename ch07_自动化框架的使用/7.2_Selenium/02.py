# 对应：第7章 自动化框架的使用
# 小节：7.2 Selenium
# 条目：7.2.3 快速上手
# 清单：02
# 说明：摘自书稿示例，未改写。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 创建 Chrome 浏览器驱动（会自动打开一个 Chrome 窗口）
driver = webdriver.Chrome()

try:
    # 打开百度
    driver.get('https://www.baidu.com')
    print(f"当前页面标题：{driver.title}")

    # 找到搜索框并输入关键词
    search_box = driver.find_element(By.ID, 'chat-textarea')
    search_box.clear()
    search_box.send_keys('Python爬虫')
    search_box.send_keys(Keys.RETURN)  # 按回车搜索

    # 等待页面加载
    time.sleep(2)
    print(f"搜索后页面标题：{driver.title}")

    # 获取当前页面 URL
    print(f"当前 URL：{driver.current_url}")

finally:
    driver.quit()  # 关闭浏览器
