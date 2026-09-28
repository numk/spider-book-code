# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.3 常用命令速查
# 清单：12
# 说明：摘自书稿示例，未改写。

# 截屏并保存到 PC
adb exec-out screencap -p > screenshot.png

# 录制屏幕（最长 3 分钟）
adb shell screenrecord /sdcard/record.mp4
adb pull /sdcard/record.mp4

# 模拟点击（坐标）
adb shell input tap 540 960

# 模拟输入文字
adb shell input text "hello"

# 模拟按键（Home 键）
adb shell input keyevent 3
