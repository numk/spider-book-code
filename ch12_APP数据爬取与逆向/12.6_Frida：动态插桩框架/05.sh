# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.6 Frida：动态插桩框架
# 条目：12.6.3 第一个 Hook 脚本：观察 MD5 方法
# 清单：05
# 说明：摘自书稿示例，未改写。

pip install frida frida-tools
npm install frida-java-bridge
frida-compile android_hook.js -o android_hook.bundle.js
python attach.py 1234 android_hook.bundle.js
