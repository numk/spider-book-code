# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.4 TLS/JA3 指纹绕过
# 清单：05
# 说明：摘自书稿示例，未改写。

import requests

resp = requests.get('https://tls.peet.ws/api/all')
data = resp.json()
print('JA3:', data['tls']['ja3'])
print('JA3 Hash:', data['tls']['ja3_hash'])
# 输出以当前运行环境为准，不应视为该库的固定常量
