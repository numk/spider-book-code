# 对应：第7章 自动化框架的使用
# 小节：7.2 Selenium
# 条目：7.2.7 实战：爬取豆瓣电影 Top250
# 清单：09
# 说明：摘自书稿示例，未改写。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def create_driver():
    """创建配置好的 Chrome 驱动"""
    options = Options()
    # options.add_argument('--headless')  # 如需无头模式，取消注释
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-blink-features=AutomationControlled')  # 隐藏自动化特征
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

def scrape_page(driver, url):
    """爬取单页电影列表"""
    driver.get(url)
    
    # 等待列表加载完成
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.grid_view .item'))
    )
    
    movies = []
    items = driver.find_elements(By.CSS_SELECTOR, '.grid_view .item')
    
    for item in items:
        try:
            rank = item.find_element(By.CSS_SELECTOR, '.pic em').text
            title = item.find_element(By.CSS_SELECTOR, '.title').text
            rating = item.find_element(By.CSS_SELECTOR, '.rating_num').text
            rating_count = item.find_element(By.CSS_SELECTOR, '.star span:last-child').text
            
            # 简介（部分电影可能没有）
            try:
                quote = item.find_element(By.CSS_SELECTOR, '.inq').text
            except:
                quote = ''
            
            movies.append({
                'rank': int(rank),
                'title': title,
                'rating': float(rating),
                'rating_count': rating_count,
                'quote': quote
            })
        except Exception as e:
            print(f"提取某条数据时出错：{e}")
    
    return movies

def get_next_page_url(driver):
    """获取下一页的 URL，如果没有下一页则返回 None"""
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, '.paginator .next a')
        return next_btn.get_attribute('href')
    except:
        return None

def main():
    driver = create_driver()
    all_movies = []
    
    url = 'https://movie.douban.com/top250'
    page = 1
    
    print("开始爬取豆瓣电影 Top250...")
    
    try:
        while url and page <= 10:  # 最多爬取 10 页（即 Top250 的全部页面）
            print(f"\n正在爬取第 {page} 页：{url}")
            movies = scrape_page(driver, url)
            all_movies.extend(movies)
            print(f"  本页获取 {len(movies)} 部电影，累计 {len(all_movies)} 部")
            
            # 礼貌延迟
            time.sleep(2)
            
            url = get_next_page_url(driver)
            page += 1
    
    except Exception as e:
        print(f"爬取过程中出错：{e}")
    finally:
        driver.quit()
    
    print(f"\n爬取完成，共获取 {len(all_movies)} 部电影")
    
    # 打印前5名
    print("\n=== 豆瓣电影 Top5 ===")
    for movie in all_movies[:5]:
        print(f"  第{movie['rank']}名：《{movie['title']}》  "
              f"评分：{movie['rating']}  {movie['rating_count']}")
        if movie['quote']:
            print(f"       「{movie['quote']}」")
    
    # 保存结果
    with open('douban_top250.json', 'w', encoding='utf-8') as f:
        json.dump(all_movies, f, ensure_ascii=False, indent=2)
    print("\n数据已保存到 douban_top250.json")

if __name__ == '__main__':
    main()
