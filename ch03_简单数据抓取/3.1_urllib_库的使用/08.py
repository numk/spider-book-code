# 对应：第3章 简单数据抓取
# 小节：3.1 urllib 库的使用
# 条目：3.1.2 urllib 库的使用
# 清单：08
# 说明：摘自书稿示例，未改写。

from urllib.parse import quote, unquote

original_string = "Hello World!"

encoded_string = quote(original_string)
print(encoded_string)
decoded_string = unquote(encoded_string)
print(decoded_string)
