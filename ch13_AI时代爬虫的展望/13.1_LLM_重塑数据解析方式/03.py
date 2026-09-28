# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.1 LLM 重塑数据解析方式
# 条目：13.1.3 结构化提取框架：instructor 与 Pydantic
# 清单：03
# 说明：摘自书稿示例，未改写。

# pip install instructor pydantic openai
import instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional
import requests
from bs4 import BeautifulSoup

# 用 instructor 包装 OpenAI 客户端
client = instructor.from_openai(OpenAI())

# 用 Pydantic 定义期望的数据结构（自带类型验证）
class ProductInfo(BaseModel):
    name: str = Field(description="商品名称")
    current_price: float = Field(description="当前售价，纯数字")
    original_price: Optional[float] = Field(None, description="原价，没有则为null")
    rating: Optional[float] = Field(None, description="评分，0-5分")
    review_count: Optional[int] = Field(None, description="评论数量")
    in_stock: bool = Field(description="是否有货")
    main_features: list[str] = Field(description="主要特性列表，最多5条")

def scrape_product(url: str) -> ProductInfo:
    """爬取并提取商品信息"""
    # 1. 获取页面
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 2. 提取 body 文本（去掉 script/style 标签，减少干扰）
    for tag in soup(['script', 'style', 'nav', 'footer']):
        tag.decompose()
    text_content = soup.get_text(separator='\n', strip=True)
    
    # 3. 用 instructor 提取结构化数据
    product = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'user',
                'content': f'从以下网页内容中提取商品信息：\n\n{text_content[:3000]}'
            }
        ],
        response_model=ProductInfo,  # 关键：指定返回模型
    )
    
    return product

# product = scrape_product('https://item.jd.com/...')
# print(product.model_dump_json(indent=2))
