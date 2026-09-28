# 对应：第9章 Scrapy 框架的使用
# 小节：9.6 Item Pipeline：数据管道
# 条目：9.6.1 数据清洗 Pipeline
# 清单：01
# 说明：摘自书稿示例，未改写。

# pipelines.py
class CleanPipeline:
    """数据清洗管道：清理价格字段，统一格式"""
    
    def process_item(self, item, spider):
        # 清洗价格字段：去掉货币符号，转为浮点数
        price_str = item.get('price', '')
        if price_str:
            try:
                item['price'] = float(
                    price_str.replace('£', '').replace('Â', '').strip()
                )
            except ValueError:
                item['price'] = 0.0
        
        # 清洗标题：去除首尾空格
        if item.get('title'):
            item['title'] = item['title'].strip()
        
        return item  # 必须 return item，否则后续管道收不到数据
