# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.2 Web Agent：爬虫的智能化升维
# 条目：13.2.2 browser-use：浏览器 Agent 库
# 清单：01
# 说明：摘自书稿示例，未改写。

# pip install browser-use
import asyncio
from browser_use import Agent
from browser_use import ChatOpenAI

async def main():
    # 创建 Agent，指定使用的 LLM
    agent = Agent(
        task="在豆瓣电影 Top250 页面，找到评分最高的10部电影，返回电影名、导演、评分",
        llm=ChatOpenAI(model='gpt-4o'),
    )
    
    # 运行 Agent，它会自主操控浏览器完成任务
    result = await agent.run(max_steps=10)
    print(result)

asyncio.run(main())
