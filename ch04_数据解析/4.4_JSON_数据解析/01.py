# 对应：第4章 数据解析
# 小节：4.4 JSON 数据解析
# 条目：4.4.1 什么是 JSON
# 清单：01
# 说明：摘自书稿示例，未改写。

book_list_json = '''
{
  "code": 0,
  "data": {"total": 2, "books": [
    {"id": 1, "title": "Python爬虫实战", "price": 79.0,
     "author": {"name": "示例作者"}, "tags": ["Python", "爬虫"]},
    {"id": 2, "title": "数据分析", "price": 59.0,
     "author": null, "tags": []}
  ]}
}
'''
