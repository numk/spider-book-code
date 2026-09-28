# 对应：第8章 反爬对抗
# 小节：8.4 验证码处理
# 条目：8.4.1 图形验证码：Tesseract OCR
# 清单：04
# 说明：摘自书稿示例，未改写。

import pytesseract
from PIL import Image

# 配置 tesseract 可执行文件路径（如果没在环境变量里, 需要指定路径）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 打开验证码图片
image = Image.open('captcha.png')

# 直接识别
captcha_text = pytesseract.image_to_string(image, config='--psm 7 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
print(f"识别结果：{captcha_text.strip()}")
