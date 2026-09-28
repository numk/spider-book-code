# 对应：第6章 并发编程与爬虫提速
# 小节：6.4 协程爬虫（asyncio + aiohttp）
# 条目：6.4.2 async/await 基础
# 清单：01
# 说明：摘自书稿示例，未改写。

import asyncio
import time

async def hello(name, delay):
    """一个简单的异步函数"""
    print(f"[{name}] 开始，等待 {delay} 秒...")
    await asyncio.sleep(delay)  # 异步等待，不阻塞其他协程
    print(f"[{name}] 完成！")
    return f"{name} 的结果"

async def main():
    """主协程，使用 asyncio.gather 并发运行多个协程"""
    start = time.time()
    
    # 并发运行三个协程
    results = await asyncio.gather(
        hello("任务A", 2),
        hello("任务B", 1),
        hello("任务C", 3),
    )
    
    print(f"\n所有任务完成，耗时：{time.time() - start:.2f} 秒")
    print(f"结果：{results}")

asyncio.run(main())
