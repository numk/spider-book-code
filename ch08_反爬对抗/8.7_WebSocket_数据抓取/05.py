# 对应：第8章 反爬对抗
# 小节：8.7 WebSocket 数据抓取
# 条目：8.7.2 websockets 库（异步方式）
# 清单：05
# 说明：摘自书稿示例，未改写。

async def with_heartbeat():
    uri = 'wss://stream.example.com/ws'

    async with websockets.connect(uri, ping_interval=None) as ws:
        # 开一个任务定时发应用层心跳
        async def send_ping():
            while True:
                await asyncio.sleep(20)
                await ws.send(json.dumps({'type': 'ping'}))

        asyncio.create_task(send_ping())

        async for raw in ws:
            msg = json.loads(raw)
            if msg.get('type') == 'pong':
                continue   # 忽略心跳回包
            print(msg)

asyncio.run(with_heartbeat())
