# 对应：第5章 数据存储
# 小节：5.3 MongoDB 数据库存储
# 条目：5.3.4 插入数据
# 清单：12
# 说明：摘自书稿示例，未改写。

books = [
    {
        'title': 'Python金融量化分析',
        'author': '张三',
        'price': 89.00,
        'tags': ['Python', '金融', '量化'],
    },
    {
        'title': 'Python数据分析实战',
        'author': '李四',
        'price': 59.00,
        'tags': ['Python', '数据分析'],
    },
    {
        'title': 'Python机器学习',
        'author': '王五',
        'price': 99.00,
        'tags': ['Python', '机器学习', 'AI'],
    }
]

result = collection.insert_many(books)
print(f"批量插入成功，共插入 {len(result.inserted_ids)} 条文档")
