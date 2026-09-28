# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.2 常见加密算法
# 清单：02
# 说明：摘自书稿示例，未改写。

import hashlib

text = 'Hello, World!'
sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
print(f'SHA-256: {sha256_hash}')
# 输出：SHA-256: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
