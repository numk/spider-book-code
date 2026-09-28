# 对应：第8章 反爬对抗
# 小节：8.4 验证码处理
# 条目：8.4.2 图形验证码：ddddocr
# 清单：09
# 说明：摘自书稿示例，未改写。

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import ddddocr
import time
import random

def get_slider_distance(slider_element, bg_element):
    """截图并计算滑动距离"""
    slider_element.screenshot('slider.png')
    bg_element.screenshot('background.png')
    
    slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    with open('slider.png', 'rb') as f:
        slider_bytes = f.read()
    with open('background.png', 'rb') as f:
        bg_bytes = f.read()
    
    result = slide.slide_match(slider_bytes, bg_bytes)
    return result['target'][0]  # 返回需要移动的 x 像素距离

def simulate_slide(driver, slider_btn, distance):
    """模拟人工滑动：加速-匀速-减速，带随机抖动"""
    action = ActionChains(driver)
    action.click_and_hold(slider_btn)
    action.perform()
    
    # 模拟人工滑动轨迹：先快后慢
    current = 0
    while current < distance:
        # 每次移动的步长随机，模拟人手的抖动
        step = random.randint(5, 20) if current < distance * 0.8 else random.randint(1, 5)
        step = min(step, distance - current)
        action.move_by_offset(step, random.randint(-2, 2))  # y 方向少量随机抖动
        action.perform()
        current += step
        time.sleep(random.uniform(0.01, 0.03))
    
    time.sleep(0.3)
    action.release().perform()
