# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.2 常见加密算法
# 清单：05
# 说明：摘自书稿示例，未改写。

import base64
import json

# 接口返回的疑似 Base64 字符串
raw = 'eyJzdGF0dXMiOiAib2siLCAiZGF0YSI6IFsxLCAyLCAzXX0='

try:
    decoded = base64.b64decode(raw).decode('utf-8')
    data = json.loads(decoded)
    print(data)
    # {'status': 'ok', 'data': [1, 2, 3]}
except Exception:
    print('不是合法的 Base64 或解码后不是 JSON')
