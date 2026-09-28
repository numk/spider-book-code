# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.6 Frida：动态插桩框架
# 条目：12.6.3 第一个 Hook 脚本：观察 MD5 方法
# 清单：06
# 说明：摘自书稿示例，未改写。

import argparse
from pathlib import Path
import sys
import frida

parser = argparse.ArgumentParser()
parser.add_argument('pid', type=int)
parser.add_argument('bundle', type=Path)
args = parser.parse_args()
device = frida.get_usb_device(timeout=5)
session = device.attach(args.pid)

def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message.get('stack', message))

try:
    script = session.create_script(args.bundle.read_text(encoding='utf-8'))
    script.on('message', on_message)
    script.load()
    print('已附加，操作教学 App 后按 Ctrl+C 结束')
    sys.stdin.read()
finally:
    session.detach()
