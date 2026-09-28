# 对应：第3章 简单数据抓取
# 小节：3.1 urllib 库的使用
# 条目：3.1.2 urllib 库的使用
# 清单：06
# 说明：摘自书稿示例，未改写。

from urllib.parse import parse_qs

query_string = "q=python&page=1"

parsed_query = parse_qs(query_string)

print(parsed_query)
