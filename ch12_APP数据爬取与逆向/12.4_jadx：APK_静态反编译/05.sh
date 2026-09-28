# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.4 jadx：APK 静态反编译
# 条目：12.4.3 jadx 常用技巧
# 清单：05
# 说明：摘自书稿示例，未改写。

# 将 APK 反编译到指定目录
jadx -d output_dir target.apk

# 仅反编译资源（不反编译代码）
jadx -r -d output_dir target.apk

# 显示更多调试信息
jadx -v -d output_dir target.apk
