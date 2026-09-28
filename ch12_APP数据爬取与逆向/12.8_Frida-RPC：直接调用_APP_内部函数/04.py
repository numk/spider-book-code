# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.8 Frida-RPC：直接调用 APP 内部函数
# 条目：12.8.2 最小签名调用
# 清单：04
# 说明：摘自书稿示例，未改写。

from pathlib import Path
import frida

device = frida.get_usb_device(timeout=10)
session = device.attach(1234)
try:
    script = session.create_script(Path("rpc_sign.bundle.js").read_text(encoding="utf-8"))
    script.load()
    print(script.exports_sync.sign("page=1"))
finally:
    session.detach()
