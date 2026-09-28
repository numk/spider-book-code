# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.3 常用命令速查
# 清单：08
# 说明：摘自书稿示例，未改写。

# 安装 APK
adb install example.apk

# 覆盖安装（保留数据）
adb install -r example.apk

# 卸载应用
adb uninstall com.example.app

# 查找已安装应用的 APK 路径（逆向分析第一步）
adb shell pm path com.example.app
# 输出：package:/data/app/~~xyz==/com.example.app-1/base.apk

# 列出所有已安装的第三方应用包名
adb shell pm list packages -3
