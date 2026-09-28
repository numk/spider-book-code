# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.3 常用命令速查
# 清单：06
# 说明：摘自书稿示例，未改写。

# 查看设备列表
adb devices

# 进入设备 Shell（交互式命令行）
adb shell

# 查看 CPU 架构（决定下载哪个 frida-server 版本）
adb shell getprop ro.product.cpu.abi
# 输出：arm64-v8a

# 查看 Android 版本
adb shell getprop ro.build.version.release
# 输出：13

# 查看设备型号
adb shell getprop ro.product.model
