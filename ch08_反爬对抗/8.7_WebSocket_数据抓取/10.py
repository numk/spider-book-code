# 对应：第8章 反爬对抗
# 小节：8.7 WebSocket 数据抓取
# 条目：8.7.4 实战：抓取币安实时行情
# 清单：10
# 说明：摘自书稿示例，未改写。

import redis.asyncio as redis
r = redis.Redis.from_url('redis://localhost:6379/0')
# 在原有接收循环内：
record = json.dumps({'price': msg['p'], 'qty': msg['q'], 'time': msg['T']})
async with r.pipeline(transaction=True) as pipe:
    pipe.lpush('btc_trades', record).ltrim('btc_trades', 0, 9999)
    await pipe.execute()
