# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.1 LLM 重塑数据解析方式
# 条目：13.1.2 LLM 直接从 HTML 提取结构化数据
# 清单：01
# 说明：摘自书稿示例，未改写。

# 使用 OpenAI API 从 HTML 中提取结构化数据
from openai import OpenAI
import json

client = OpenAI()

def extract_with_llm(html_content: str, schema: dict) -> dict:
    """
    使用 LLM 从 HTML 中提取结构化数据
    schema: 字段说明字典（此处不是正式 JSON Schema）
    """
    prompt = f"""
请从以下 HTML 内容中，提取符合字段说明 的结构化数据。
只返回 JSON 数据，不要包含任何解释文字。

期望的数据结构：
{json.dumps(schema, ensure_ascii=False, indent=2)}

HTML 内容：
{html_content[:4000]}
"""
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': '你是一个数据提取助手，从HTML中提取结构化数据，只返回JSON格式。'},
            {'role': 'user', 'content': prompt}
        ],
        response_format={'type': 'json_object'}  # 强制返回 JSON
    )
    
    return json.loads(response.choices[0].message.content)


# 示例：提取商品信息
html = """
<div class="product-detail">
    <h1 class="prod-name">Apple AirPods Pro 第2代</h1>
    <div class="price-block">
        <span class="current-price">¥1,799</span>
        <span class="original-price">¥1,999</span>
    </div>
    <div class="rating">
        <span class="score">4.8</span>
        <span class="count">（23,421条评价）</span>
    </div>
    <p class="description">主动降噪，通透模式，Adaptive Audio...</p>
</div>
"""

schema = {
    "name": "商品名称（字符串）",
    "current_price": "当前价格（浮点数，去掉货币符号）",
    "original_price": "原价（浮点数）",
    "rating": "评分（浮点数）",
    "review_count": "评论数（整数）",
    "description": "商品描述（字符串）"
}

result = extract_with_llm(html, schema)
print(json.dumps(result, ensure_ascii=False, indent=2))
