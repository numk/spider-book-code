# 对应：第8章 反爬对抗
# 小节：8.4 验证码处理
# 条目：8.4.2 图形验证码：ddddocr
# 清单：08
# 说明：摘自书稿示例，未改写。

import ddddocr

slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

# 读取滑块图片和背景图片
with open('slider.png', 'rb') as f:
    slider_bytes = f.read()
with open('background.png', 'rb') as f:
    bg_bytes = f.read()

# 计算滑块需要移动的距离
result = slide.slide_match(slider_bytes, bg_bytes)
print(f"滑块移动距离：{result}")
