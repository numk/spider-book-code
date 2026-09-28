# 对应：第13章 AI 时代爬虫的发展趋势与展望
# 小节：13.4 云原生爬虫架构的演进
# 条目：13.4.2 Serverless 爬虫：按需付费，按需扩展
# 清单：01
# 说明：摘自书稿示例，未改写。

# 阿里云函数计算 爬虫函数示例
import requests
import json
import oss2

def handler(event, context):
    """
    函数计算入口
    event: 触发事件（包含爬取参数）
    """
    params = json.loads(event)
    url = params['url']
    task_id = params['task_id']
    
    # 爬取数据
    response = requests.get(url, timeout=10, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...'
    })
    
    # 解析数据
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one('h1').get_text(strip=True) if soup.select_one('h1') else ''
    
    result = {
        'task_id': task_id,
        'url': url,
        'title': title,
        'status': response.status_code,
    }
    
    # 将结果写入 OSS（对象存储）
    auth = oss2.Auth(context.credentials.access_key_id,
                     context.credentials.access_key_secret)
    bucket = oss2.Bucket(auth, 'oss-cn-hangzhou.aliyuncs.com', 'my-spider-bucket')
    bucket.put_object(f'results/{task_id}.json', json.dumps(result, ensure_ascii=False))
    
    return result
