# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.3 反爬技术的 AI 化升级
# 条目：13.3.2 AI 生成的动态验证码
# 清单：01
# 说明：摘自书稿示例，未改写。

import base64
from openai import OpenAI

client = OpenAI()

def solve_captcha_with_llm(image_path: str, question: str) -> str:
    """使用多模态 LLM 解答视觉验证码"""
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'image_url',
                        'image_url': {
                            'url': f'data:image/png;base64,{image_data}'
                        }
                    },
                    {
                        'type': 'text',
                        'text': f'这是一个验证码题目：{question}\n请告诉我正确答案（只需要回答答案，不需要解释）'
                    }
                ]
            }
        ]
    )
    
    return response.choices[0].message.content.strip()

# 示例：解答"选择所有包含红绿灯的图片"类型的验证码
# answer = solve_captcha_with_llm('captcha.png', '请选择所有包含自行车的图片编号（1-9）')
