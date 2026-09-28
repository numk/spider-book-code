# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.4 jadx：APK 静态反编译
# 条目：12.4.2 分析加密参数的完整流程
# 清单：04
# 说明：摘自书稿示例，未改写。

import hashlib
from collections import OrderedDict

APP_KEY = 'your_app_key_here'
APP_SECRET = 'your_app_secret_here'

def generate_sign(params: dict) -> str:
    """复现 APP 的签名算法"""
    # 按 key 排序
    sorted_params = OrderedDict(sorted(params.items()))
    
    # 拼接 key=value&
    parts = [f"{k}={v}" for k, v in sorted_params.items()]
    raw_str = '&'.join(parts) + f'&secret={APP_SECRET}'
    
    # MD5
    return hashlib.md5(raw_str.encode('utf-8')).hexdigest()

# 测试
import time
params = {
    'page': '1',
    'size': '20',
    'timestamp': str(int(time.time())),
}
sign = generate_sign(params)
print(f"sign = {sign}")

# 带 sign 参数发起请求
import requests
params['sign'] = sign
response = requests.get('https://api.example.com/api/v2/content/list', params=params)
print(response.json())
