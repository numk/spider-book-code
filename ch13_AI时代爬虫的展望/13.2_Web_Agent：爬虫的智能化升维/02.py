# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.2 Web Agent：爬虫的智能化升维
# 条目：13.2.3 Playwright + LLM 的组合实践
# 清单：02
# 说明：摘自书稿示例，未改写。

import asyncio
from playwright.async_api import async_playwright
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def llm_decide_action(page_content: str, task: str) -> dict:
    """让 LLM 根据当前页面状态，决定下一步操作"""
    response = await client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'system',
                'content': '''你是一个浏览器操作助手。根据当前页面内容和任务目标，
                决定下一步操作。返回 JSON 格式：
                {"action": "click|type|extract|done", "selector": "CSS选择器", 
                 "text": "输入文本", "data": "提取的数据"}'''
            },
            {
                'role': 'user',
                'content': f'任务：{task}\n\n当前页面内容（节选）：\n{page_content[:2000]}'
            }
        ],
        response_format={'type': 'json_object'}
    )
    import json
    return json.loads(response.choices[0].message.content)

async def smart_crawler(url: str, task: str):
    """智能爬虫：LLM 自主决策操作流程"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        
        results = []
        max_steps = 10  # 最多执行10步，防止无限循环
        
        for step in range(max_steps):
            # 获取当前页面的文本内容
            content = await page.evaluate('''() => {
                // 提取页面主要文本，过滤脚本和样式
                const body = document.body.cloneNode(true);
                body.querySelectorAll("script, style, nav").forEach(e => e.remove());
                return body.innerText.substring(0, 3000);
            }''')
            
            # 让 LLM 决定下一步
            action = await llm_decide_action(content, task)
            print(f'[步骤 {step+1}] LLM 决策：{action}')
            
            if action['action'] == 'done':
                results.append(action.get('data', ''))
                break
            elif action['action'] == 'click':
                await page.click(action['selector'])
                await page.wait_for_timeout(1000)
            elif action['action'] == 'type':
                await page.fill(action['selector'], action['text'])
                await page.press(action['selector'], 'Enter')
                await page.wait_for_timeout(1000)
            elif action['action'] == 'extract':
                results.append(action.get('data', ''))
        
        await browser.close()
        return results

# asyncio.run(smart_crawler('https://www.douban.com/group/explore', '找到最热门的5个豆瓣小组名称和成员数'))
