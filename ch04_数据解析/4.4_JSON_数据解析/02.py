# 对应：第4章 数据解析
# 小节：4.4 JSON 数据解析
# 条目：4.4.3 Python 中的 json 模块
# 清单：02
# 说明：摘自书稿示例，未改写。

import json
data = json.loads(book_list_json)
print(data['data']['books'][0]['title'])
encoded = json.dumps(data, ensure_ascii=False, indent=2)
assert json.loads(encoded) == data
