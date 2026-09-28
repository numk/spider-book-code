# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.11 综合实战：完整的 APP 数据爬取流程
# 条目：12.11.4 阶段四：验证签名复现
# 清单：06
# 说明：摘自书稿示例，未改写。

import hashlib
import hmac

raw = "category=1&page=1&size=20&ts=1704067200&nonce=8f3a2b1c"
key = b"ExAmPleS3cr3tK3y2024"  # 教学数据
signature = hmac.new(key, raw.encode("utf-8"), hashlib.sha256).hexdigest()
print(signature)
