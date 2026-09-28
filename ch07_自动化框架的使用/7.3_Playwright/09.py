# 对应：第7章 自动化框架的使用
# 小节：7.3 Playwright
# 条目：7.3.7 实战：爬取 JS 渲染的电影数据
# 清单：09
# 说明：摘自书稿示例，未改写。

from playwright.sync_api import sync_playwright
import json
import time

def scrape_spa_movies():
    """爬取单页应用（SPA）渲染的电影列表"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 拦截图片资源，加快加载
        def block_images(route, request):
            if request.resource_type == 'image':
                route.abort()
            else:
                route.continue_()
        page.route('**/*', block_images)
        
        all_movies = []
        
        for page_num in range(1, 11):
            url = f'https://spa1.scrape.center/page/{page_num}'
            print(f"正在爬取第 {page_num} 页...")
            
            page.goto(url)
            
            # 等待电影卡片加载完成
            page.wait_for_selector('.el-card', timeout=15000)
            
            # 提取电影数据
            cards = page.query_selector_all('.el-card')
            for card in cards:
                try:
                    title = card.query_selector('h2').inner_text()
                    
                    # 评分
                    try:
                        score = card.query_selector('.score').inner_text()
                    except:
                        score = 'N/A'
                    
                    # 类别
                    categories = [c.inner_text() for c in card.query_selector_all('.categories button')]
                    
                    # 上映时间
                    try:
                        date = card.query_selector('.info:last-child span:last-child').inner_text()
                    except:
                        date = ''
                    
                    all_movies.append({
                        'title': title,
                        'score': score,
                        'categories': categories,
                        'date': date,
                        'page': page_num
                    })
                except Exception as e:
                    pass
            
            print(f"  第 {page_num} 页获取 {len(cards)} 部电影")
            time.sleep(1)  # 礼貌延迟
        
        browser.close()
        return all_movies

if __name__ == '__main__':
    movies = scrape_spa_movies()
    print(f"\n共爬取 {len(movies)} 部电影")
    
    for movie in movies[:5]:
        print(f"《{movie['title']}》  评分：{movie['score']}  "
              f"类别：{'/'.join(movie['categories'])}")
    
    with open('spa_movies.json', 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)
    print("\n数据已保存到 spa_movies.json")
