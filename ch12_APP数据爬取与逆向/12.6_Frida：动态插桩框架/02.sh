# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.6 Frida：动态插桩框架
# 条目：12.6.2 环境搭建
# 清单：02
# 说明：摘自书稿示例，未改写。

# 解压后重命名
mv frida-server-16.1.4-android-arm64 frida-server

# 推送到设备
adb push frida-server /data/local/tmp/

# 赋予执行权限
adb shell chmod 755 /data/local/tmp/frida-server

# 以 root 权限启动（需要 root 权限）
adb shell su -c "/data/local/tmp/frida-server &"
