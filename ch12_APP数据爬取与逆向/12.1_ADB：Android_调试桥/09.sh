# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.3 常用命令速查
# 清单：09
# 说明：摘自书稿示例，未改写。

# 查看正在运行的进程
adb shell ps -A | grep com.example

# 以 root 身份执行命令（需要 root 权限）
adb shell su -c "命令"

# 修改文件权限（如给 frida-server 添加执行权限）
adb shell chmod 755 /data/local/tmp/frida-server

# 启动 frida-server（后台运行）
adb shell su -c "/data/local/tmp/frida-server &"
