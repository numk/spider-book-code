# 对应：第9章 Scrapy 框架的使用
# 小节：9.6 Item Pipeline：数据管道
# 条目：9.6.2 去重 Pipeline
# 清单：02
# 说明：摘自书稿示例，未改写。

from scrapy.exceptions import DropItem

class DuplicatesPipeline:
    """去重管道：丢弃重复的 URL"""
    
    def __init__(self):
        self.seen_urls = set()
    
    def process_item(self, item, spider):
        url = item.get('detail_url') or item.get('url', '')
        if url in self.seen_urls:
            raise DropItem(f"重复数据，丢弃：{item.get('title', '')}")
        self.seen_urls.add(url)
        return item
