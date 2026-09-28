# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.1 ADB：Android 调试桥
# 条目：12.1.4 提取 APK 的完整流程
# 清单：13
# 说明：摘自书稿示例，未改写。

# 第一步：找到应用的包名
# 方法一：在 APP 运行时查进程
adb shell ps -A | grep -i "目标APP关键词"

# 方法二：列出所有第三方应用，配合关键词过滤
adb shell pm list packages -3 | grep example

# 第二步：获取 APK 路径
adb shell pm path com.example.app
# 输出：package:/data/app/~~AbCdEfGh==/com.example.app-1/base.apk

# 第三步：拉取 APK 到本地
adb pull /data/app/~~AbCdEfGh==/com.example.app-1/base.apk ./example.apk

# 如果 APP 有多个 APK（split APKs），还需要拉取其他部分
adb shell pm path com.example.app
# 可能输出多行：
# package:/data/app/.../base.apk
# package:/data/app/.../split_config.arm64_v8a.apk
# package:/data/app/.../split_config.zh.apk
