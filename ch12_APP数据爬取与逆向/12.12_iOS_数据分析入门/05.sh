# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.12 iOS 数据分析入门
# 条目：12.12.5 观察一个 Objective-C 字符串方法
# 清单：05
# 说明：摘自书稿示例，未改写。

npm install frida-objc-bridge
frida-compile ios_hook.js -o ios_hook.bundle.js
frida -U -p 1234 -l ios_hook.bundle.js
