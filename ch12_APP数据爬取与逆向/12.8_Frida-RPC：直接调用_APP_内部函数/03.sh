# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.8 Frida-RPC：直接调用 APP 内部函数
# 条目：12.8.2 最小签名调用
# 清单：03
# 说明：摘自书稿示例，未改写。

npm install frida-java-bridge
pip install frida frida-tools
frida-compile rpc_sign.js -o rpc_sign.bundle.js
