# 对应：第6章 并发编程与爬虫提速
# 小节：6.3 多进程爬虫
# 条目：6.3.2 ProcessPoolExecutor 的使用
# 清单：01
# 说明：摘自书稿示例，未改写。

from concurrent.futures import ProcessPoolExecutor
import time
import math

def is_prime(n):
    """判断一个数是否为质数（CPU 密集型计算）"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    """统计范围内质数的个数"""
    count = sum(1 for n in range(start, end) if is_prime(n))
    return start, end, count

if __name__ == '__main__':
    # 将 1 到 1000000 拆分为 4 段，分别交给不同进程处理
    ranges = [(1, 250001), (250001, 500001), (500001, 750001), (750001, 1000001)]
    
    # 串行版本
    start = time.time()
    total_serial = 0
    for s, e in ranges:
        _, _, cnt = count_primes_in_range(s, e)
        total_serial += cnt
    print(f"串行耗时：{time.time() - start:.2f} 秒，质数个数：{total_serial}")
    
    # 多进程版本
    start = time.time()
    total_mp = 0
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(count_primes_in_range, s, e) for s, e in ranges]
        for future in futures:
            s, e, cnt = future.result()
            total_mp += cnt
            print(f"  [{s}, {e}) 范围内找到 {cnt} 个质数")
    print(f"多进程耗时：{time.time() - start:.2f} 秒，质数个数：{total_mp}")
