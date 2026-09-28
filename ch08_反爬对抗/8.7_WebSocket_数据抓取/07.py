# 对应：第8章 反爬对抗
# 小节：8.7 WebSocket 数据抓取
# 条目：8.7.4 实战：抓取币安实时行情
# 清单：07
# 说明：摘自书稿示例，未改写。

import asyncio
import websockets
import json
from datetime import datetime

async def binance_trade_stream():
    uri = 'wss://stream.binance.com:9443/ws/btcusdt@trade'

    print('开始接收 BTC/USDT 实时成交数据...')
    async with websockets.connect(uri) as ws:
        async for raw in ws:
            msg = json.loads(raw)
            # 字段说明：p=价格, q=数量, T=成交时间戳, m=是否买方挂单
            price    = float(msg['p'])
            qty      = float(msg['q'])
            ts       = datetime.fromtimestamp(msg['T'] / 1000)
            side     = '卖' if msg['m'] else '买'
            print(f'[{ts:%H:%M:%S}] {side}单  价格: {price:>12.2f}  数量: {qty:.6f} BTC')

asyncio.run(binance_trade_stream())
