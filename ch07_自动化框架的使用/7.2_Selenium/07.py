# 对应：第7章 自动化框架的使用
# 小节：7.2 Selenium
# 条目：7.2.5 等待机制
# 清单：07
# 说明：摘自书稿示例，未改写。

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 最多等待 10 秒，直到指定元素出现在 DOM 中
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'some-element'))
)

# 等待元素可点击
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-btn'))
)
