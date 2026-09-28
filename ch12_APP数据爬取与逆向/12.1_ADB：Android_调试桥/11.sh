# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.3 常用命令速查
# 清单：11
# 说明：摘自书稿示例，未改写。

# 将 PC 的 27042 端口转发到手机的 27042 端口（frida-server 默认端口）
adb forward tcp:27042 tcp:27042

# 查看当前所有转发规则
adb forward --list

# 移除转发规则
adb forward --remove tcp:27042
