# 对应：第8章 反爬对抗
# 小节：8.6 高级反爬与浏览器指纹
# 条目：8.6.4 TLS/JA3 指纹绕过
# 清单：07
# 说明：摘自书稿示例，未改写。

from curl_cffi import requests as cffi_requests

# impersonate 参数指定要模拟的浏览器版本
response = cffi_requests.get(
    'https://tls.peet.ws/api/all',
    impersonate='chrome124',   # 模拟 Chrome 124 的 TLS 指纹
)
data = response.json()
print('JA3 Hash:', data['tls']['ja3_hash'])
# 浏览器档案模拟握手特征；扩展排列可能使 JA3 改变
