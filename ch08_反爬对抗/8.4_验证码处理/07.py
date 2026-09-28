# 对应：第8章 反爬对抗
# 小节：8.4 验证码处理
# 条目：8.4.2 图形验证码：ddddocr
# 清单：07
# 说明：摘自书稿示例，未改写。

import ddddocr

ocr = ddddocr.DdddOcr(show_ad=False)  # show_ad=False 关闭广告提示

# 读取验证码图片字节流
with open('captcha.png', 'rb') as f:
    image_bytes = f.read()

# 识别
result = ocr.classification(image_bytes)
print(f"识别结果：{result}")
