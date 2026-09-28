# 对应：第8章 反爬对抗
# 小节：8.7 WebSocket 数据抓取
# 条目：8.7.3 websocket-client 库（同步方式）
# 清单：06
# 说明：摘自书稿示例，未改写。

import websocket

ws = websocket.create_connection(
    'wss://stream.binance.com:9443/ws/btcusdt@trade', timeout=15)
try:
    print(ws.recv())
finally:
    ws.close()
