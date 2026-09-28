# 对应：第6章 并发编程与爬虫提速
# 小节：6.2 多线程爬虫
# 条目：6.2.2 线程安全与锁
# 清单：02
# 说明：摘自书稿示例，未改写。

import threading

balance = 100  # 账户余额（元）
barrier = threading.Barrier(2)  # 强制两个线程都查完余额后再扣款

def withdraw(amount):
    global balance
    if balance >= amount:   # 第一步：检查余额是否够扣
        barrier.wait()       # 等另一个线程也检查完，模拟两笔请求同时到达
        balance -= amount    # 第二步：扣款
        print(f"取款 {amount} 元成功，余额剩余 {balance} 元")
    else:
        print(f"取款 {amount} 元失败，余额不足")

threads = [threading.Thread(target=withdraw, args=(80,)) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"最终余额：{balance} 元")
