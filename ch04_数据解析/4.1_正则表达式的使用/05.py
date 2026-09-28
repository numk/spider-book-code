# 对应：第4章 数据解析
# 小节：4.1 正则表达式的使用
# 条目：4.1.3 re 模块的常用方法
# 清单：05
# 说明：摘自书稿示例，未改写。

import re

# 爬取到的带有 HTML 标签的文本
dirty_text = "<p>这是一段<strong>带有标签</strong>的<em>文本内容</em>。</p>"

# 去除所有 HTML 标签
clean_text = re.sub(r'<.*?>', '', dirty_text)
print(clean_text)
