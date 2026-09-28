# 对应：第8章 反爬对抗
# 小节：8.4 验证码处理
# 条目：8.4.3 第三方验证码识别服务
# 清单：10
# 说明：摘自书稿示例，未改写。

import requests
import base64

def recognize_with_ttshitu(image_path, username, password, typeid=3):
    """
    使用图鉴识别验证码
    typeid: 验证码类型 (3=数字+字母, 6=纯数字, 10=中文)
    """
    with open(image_path, 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    
    payload = {
        'username': username,
        'password': password,
        'typeid': typeid,
        'image': image_b64
    }
    
    response = requests.post(
        'http://api.ttshitu.com/predict',
        json=payload,
        timeout=15
    )
    
    result = response.json()
    if result.get('success'):
        return result['data']['result']
    else:
        raise Exception(f"识别失败：{result.get('message')}")

# 使用示例
try:
    text = recognize_with_ttshitu(
        image_path='captcha.png',
        username='your_username',
        password='your_password',
        typeid=3
    )
    print(f"识别结果：{text}")
except Exception as e:
    print(f"错误：{e}")
