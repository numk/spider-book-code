# 对应：第10章 分布式爬虫的设计
# 小节：10.2 分布式爬虫的核心组件
# 条目：10.2.2 URL 去重
# 清单：03
# 说明：摘自书稿示例，未改写。

# 安装：pip install bloom-filter2
from bloom_filter2 import BloomFilter

# 预估 URL 总量 1000 万，允许误判率 0.001%
bloom = BloomFilter(max_elements=10_000_000, error_rate=0.00001)

def should_crawl(url: str) -> bool:
    if url in bloom:
        return False  # 可能已爬取（存在极小误判概率）
    bloom.add(url)
    return True
