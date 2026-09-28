# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.3 常用命令速查
# 清单：07
# 说明：摘自书稿示例，未改写。

# 将 PC 上的文件推送到手机
adb push <本地路径> <设备路径>

# 示例：推送 frida-server 到手机
adb push frida-server /data/local/tmp/

# 将手机上的文件拉取到 PC
adb pull <设备路径> <本地路径>

# 示例：拉取 APK 到当前目录
adb pull /data/app/~~xyz==/com.example.app-1/base.apk ./example.apk
