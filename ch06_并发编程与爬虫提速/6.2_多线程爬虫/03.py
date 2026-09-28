# 对应：第6章 并发编程与爬虫提速
# 小节：6.2 多线程爬虫
# 条目：6.2.2 线程安全与锁
# 清单：03
# 说明：摘自书稿示例，未改写。

import threading

balance = 100
lock = threading.Lock()  # 创建锁对象

def withdraw(amount):
    global balance
    with lock:               # 检查和扣款整体加锁，中途不会被其他线程打断
        if balance >= amount:
            balance -= amount
            print(f"取款 {amount} 元成功，余额剩余 {balance} 元")
        else:
            print(f"取款 {amount} 元失败，余额不足")

threads = [threading.Thread(target=withdraw, args=(80,)) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"最终余额：{balance} 元")
