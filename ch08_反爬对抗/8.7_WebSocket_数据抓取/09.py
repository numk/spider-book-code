# 对应：第8章 反爬对抗
# 小节：8.7 WebSocket 数据抓取
# 条目：8.7.4 实战：抓取币安实时行情
# 清单：09
# 说明：摘自书稿示例，未改写。

uri = 'wss://stream.binance.com:9443/stream?streams=btcusdt@trade/ethusdt@trade'
# 在原有 async for raw in ws 循环内：
envelope = json.loads(raw)
symbol = envelope['stream'].split('@')[0].upper()
msg = envelope['data']
