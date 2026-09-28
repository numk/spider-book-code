# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.3 Referer 防盗链
# 清单：04
# 说明：摘自书稿示例，未改写。

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://example.com/list',  # 伪装成从列表页跳转而来
}

response = requests.get('https://example.com/detail/123', headers=headers)
