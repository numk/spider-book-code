# 对应：第4章 数据解析
# 小节：4.1 正则表达式的使用
# 条目：4.1.3 re 模块的常用方法
# 清单：03
# 说明：摘自书稿示例，未改写。

import re

text = "商品价格：¥128.00，库存：500件"

match = re.search(r'¥(\d+\.\d+)', text)
if match:
    price = match.group(1)
    print(f"价格是：{price}")
