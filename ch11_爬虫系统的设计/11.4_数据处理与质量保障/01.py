# 对应：第11章 爬虫系统的设计
# 小节：11.4 数据处理与质量保障
# 条目：11.4.1 数据清洗
# 清单：01
# 说明：摘自书稿示例，未改写。

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductItem:
    title: str
    price: str
    url: str
    rating: Optional[str] = None


def clean_price(raw_price: str) -> Optional[float]:
    """将价格字符串转换为浮点数"""
    if not raw_price:
        return None
    cleaned = re.sub(r"[^\d.]", "", raw_price)
    try:
        return float(cleaned)
    except ValueError:
        return None


def clean_title(raw_title: str) -> str:
    """清理标题：去除多余空白、特殊字符"""
    if not raw_title:
        return ""
    return re.sub(r"\s+", " ", raw_title).strip()


def validate_url(url: str) -> bool:
    """简单校验 URL 格式"""
    return bool(re.match(r"^https?://", url))


def clean_item(raw: dict) -> Optional[ProductItem]:
    """清洗并校验一条原始数据，返回 None 表示数据无效"""
    title = clean_title(raw.get("title", ""))
    price = clean_price(raw.get("price", ""))
    url = raw.get("url", "")

    if not title or price is None or not validate_url(url):
        return None

    return ProductItem(
        title=title,
        price=str(price),
        url=url,
        rating=raw.get("rating"),
    )
