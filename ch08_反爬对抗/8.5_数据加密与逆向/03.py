# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.2 常见加密算法
# 清单：03
# 说明：摘自书稿示例，未改写。

import base64

# 编码：字节 → Base64 字符串
data = '{"user_id": 123, "ts": 1704067200}'
encoded = base64.b64encode(data.encode('utf-8')).decode('utf-8')
print('编码结果:', encoded)
# 编码结果: eyJ1c2VyX2lkIjogMTIzLCAidHMiOiAxNzA0MDY3MjAwfQ==

# 解码：Base64 字符串 → 原始字节
decoded = base64.b64decode(encoded).decode('utf-8')
print('解码结果:', decoded)
# 解码结果: {"user_id": 123, "ts": 1704067200}
