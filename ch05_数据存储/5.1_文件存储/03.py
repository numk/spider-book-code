# 对应：第5章 数据存储
# 小节：5.1 文件存储
# 条目：5.1.2 CSV 文件的存储
# 清单：03
# 说明：摘自书稿示例，未改写。

import csv

with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)  # 一次性写入所有行
