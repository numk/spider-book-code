# 对应：第4章 数据解析
# 小节：4.4 JSON 数据解析
# 条目：4.4.7 处理嵌套 JSON 数据
# 清单：07
# 说明：摘自书稿示例，未改写。

for book in data['data']['books']:
    author = book.get('author')
    name = author.get('name', '未知作者') if isinstance(author, dict) else '未知作者'
    tags = book.get('tags') or []
    print('{} / {} / {}'.format(book['title'], name, '、'.join(tags)))
