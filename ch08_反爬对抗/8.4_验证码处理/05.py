# 对应：第8章 反爬对抗
# 小节：8.4 验证码处理
# 条目：8.4.1 图形验证码：Tesseract OCR
# 清单：05
# 说明：摘自书稿示例，未改写。

import pytesseract
from PIL import Image, ImageFilter, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_captcha(image_path):
    """验证码图像预处理"""
    image = Image.open(image_path)
    
    # 转换为灰度图
    image = image.convert('L')
    
    # 增强对比度
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    
    # 二值化：像素值小于 128 变为纯黑，否则变为纯白
    threshold = 128
    image = image.point(lambda x: 0 if x < threshold else 255)
    
    # 中值滤波去除噪点
    image = image.filter(ImageFilter.MedianFilter(size=3))
    
    return image

image = preprocess_captcha('captcha.png')
text = pytesseract.image_to_string(image, config='--psm 7')
print(f"识别结果：{text.strip()}")
