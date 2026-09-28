# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.2 常见加密算法
# 清单：01
# 说明：摘自书稿示例，未改写。

import hashlib

# 一行实现 MD5
text = 'Hello, World!'
md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
print(f'MD5: {md5_hash}')
# 输出：MD5: 65a8e27d8879283831b664bd8b7f0ad4
