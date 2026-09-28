# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.4 提取 APK 的完整流程
# 清单：14
# 说明：摘自书稿示例，未改写。

adb shell cp /data/app/.../base.apk /sdcard/base.apk
adb pull /sdcard/base.apk ./example.apk
