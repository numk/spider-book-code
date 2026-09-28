# 对应：第4章 数据解析
# 小节：4.4 JSON 数据解析
# 条目：4.4.5 实战：爬取 API 接口的 JSON 数据
# 清单：06
# 说明：摘自书稿示例，未改写。

import json
data = json.loads(book_list_json)
for book in data['data']['books']:
    print('{}：{}'.format(book['title'], book['price']))
