# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.2 常见加密算法
# 清单：04
# 说明：摘自书稿示例，未改写。

import base64

data = b'\xfb\xff\xfe'  # 包含 +/= 的典型数据

# 标准 Base64
std = base64.b64encode(data).decode()
print('标准:', std)          # +//+

# URL-safe Base64
safe = base64.urlsafe_b64encode(data).decode()
print('URL-safe:', safe)     # -__-

# 解码时也要对应使用 urlsafe 版本
original = base64.urlsafe_b64decode(safe)
print('还原:', original)     # b'\xfb\xff\xfe'
