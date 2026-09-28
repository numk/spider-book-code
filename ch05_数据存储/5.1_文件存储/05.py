# 对应：第5章 数据存储
# 小节：5.1 文件存储
# 条目：5.1.2 CSV 文件的存储
# 清单：05
# 说明：摘自书稿示例，未改写。

with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
