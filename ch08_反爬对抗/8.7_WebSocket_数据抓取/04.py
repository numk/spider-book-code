# 对应：第8章 反爬对抗
# 小节：8.7 WebSocket 数据抓取
# 条目：8.7.2 websockets 库（异步方式）
# 清单：04
# 说明：摘自书稿示例，未改写。

import asyncio
import websockets
import json

async def subscribe():
    uri = 'wss://stream.example.com/ws/market'
    headers = {
        'Origin': 'https://www.example.com',
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/124.0.0.0 Safari/537.36'
        ),
        'Cookie': 'your_session_cookie_here',
    }

    async with websockets.connect(uri, additional_headers=headers) as ws:
        # 发送订阅指令（格式来自 DevTools Messages 面板）
        sub_msg = json.dumps({
            'type': 'subscribe',
            'channel': 'ticker',
            'symbol': 'BTC-USDT',
        })
        await ws.send(sub_msg)

        # 持续接收数据
        async for raw in ws:
            data = json.loads(raw)
            print(data)

asyncio.run(subscribe())
