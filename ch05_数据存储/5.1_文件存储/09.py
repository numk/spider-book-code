# 对应：第5章 数据存储
# 小节：5.1 文件存储
# 条目：5.1.3 JSON 文件的存储
# 清单：09
# 说明：摘自书稿示例，未改写。

import json
from pathlib import Path

data = [
    {'书籍名称': 'Python 爬虫实战', '作者': '范传辉', '出版日期': '2025-03-15', '价格': 79.0},
    {'书籍名称': 'Python 金融量化分析', '作者': '张三', '出版日期': '2025-02-15', '价格': 89.0},
]

# 将 Python 对象写入 JSON 文件
with Path('data.json').open( 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("写入成功！")

# 从 JSON 文件读取数据
with Path('data.json').open( 'r', encoding='utf-8') as f:
    data_loaded = json.load(f)

print(f"读取到 {len(data_loaded)} 条记录")
for item in data_loaded:
    print(f"书名：{item['书籍名称']}，价格：{item['价格']}")
