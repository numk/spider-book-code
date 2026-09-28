# 对应：第8章 反爬对抗
# 小节：8.7 WebSocket 数据抓取
# 条目：8.7.2 websockets 库（异步方式）
# 清单：03
# 说明：摘自书稿示例，未改写。

import asyncio
import websockets
import json

async def main():
    uri = 'wss://echo.websocket.org'   # 公开测试服务器，原样回传消息

    async with websockets.connect(uri) as ws:
        # 发送消息
        await ws.send('Hello WebSocket')
        # 接收回应
        reply = await ws.recv()
        print('收到:', reply)

asyncio.run(main())
