# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.3 常用命令速查
# 清单：10
# 说明：摘自书稿示例，未改写。

# 查看实时日志（全量）
adb logcat

# 过滤指定标签的日志（Xposed 模块日志）
adb logcat -s Xposed

# 过滤指定包名的日志
adb logcat --pid=$(adb shell pidof com.example.app)

# 清空日志缓冲区后再开始抓取
adb logcat -c && adb logcat
