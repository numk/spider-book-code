# 对应：第6章 并发编程与爬虫提速
# 小节：6.3 多进程爬虫
# 条目：6.3.3 进程间通信：Queue
# 清单：02
# 说明：摘自书稿示例，未改写。

from multiprocessing import Process, Queue
import requests
from lxml import etree

def crawler_process(url_queue, result_queue, worker_id):
    """爬虫子进程：从 url_queue 取 URL，爬取后放入 result_queue"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    while True:
        url = url_queue.get()
        if url is None:  # 收到结束信号
            print(f"[进程{worker_id}] 收到结束信号，退出")
            break
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            tree = etree.HTML(response.text)
            title = tree.xpath('string(//title)').strip()
            result_queue.put({'url': url, 'title': title, 'status': response.status_code})
            print(f"[进程{worker_id}] 完成：{url[:50]}")
        except Exception as e:
            result_queue.put({'url': url, 'title': None, 'status': None, 'error': str(e)})

if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://httpbin.org/get',
        'https://httpbin.org/ip',
        'https://httpbin.org/headers',
        'https://httpbin.org/user-agent',
        'https://httpbin.org/uuid',
    ]
    
    url_queue = Queue()
    result_queue = Queue()
    
    # 将 URL 放入队列
    for url in urls:
        url_queue.put(url)
    
    NUM_WORKERS = 3
    # 发送结束信号（每个进程一个 None）
    for _ in range(NUM_WORKERS):
        url_queue.put(None)
    
    # 启动子进程
    processes = []
    for i in range(NUM_WORKERS):
        p = Process(target=crawler_process, args=(url_queue, result_queue, i + 1))
        processes.append(p)
        p.start()
    
    # 等待所有子进程完成
    for p in processes:
        p.join()
    
    # 收集结果
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    print(f"\n共爬取 {len(results)} 个页面：")
    for r in results:
        if r.get('title'):
            print(f"  [{r['status']}] {r['title'][:30]} <- {r['url'][:40]}")
        else:
            print(f"  [失败] {r['url'][:40]} 错误：{r.get('error', '')}")
