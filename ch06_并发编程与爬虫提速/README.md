# 第6章 并发编程与爬虫提速

本目录中的文件从书稿对应章节原样抽出，只在支持注释的语言里加了来源说明。
片段示例不一定能单独运行，请对照书中上下文阅读。

## 6.2 多线程爬虫

- `6.2_多线程爬虫/01.py`：6.2.1 threading 模块基础（python）
- `6.2_多线程爬虫/02.py`：6.2.2 线程安全与锁（python）
- `6.2_多线程爬虫/03.py`：6.2.2 线程安全与锁（python）
- `6.2_多线程爬虫/04.py`：6.2.3 线程池：ThreadPoolExecutor（python）
- `6.2_多线程爬虫/05.py`：6.2.4 实战：多线程爬取图书网站（python）
## 6.3 多进程爬虫

- `6.3_多进程爬虫/01.py`：6.3.2 ProcessPoolExecutor 的使用（python）
- `6.3_多进程爬虫/02.py`：6.3.3 进程间通信：Queue（python）
- `6.3_多进程爬虫/03.py`：6.3.4 实战：多进程分网站爬取（python）
## 6.4 协程爬虫（asyncio + aiohttp）

- `6.4_协程爬虫（asyncio_+_aiohttp）/01.py`：6.4.2 async/await 基础（python）
- `6.4_协程爬虫（asyncio_+_aiohttp）/02.sh`：6.4.3 安装 aiohttp（bash）
- `6.4_协程爬虫（asyncio_+_aiohttp）/03.py`：6.4.4 基本异步爬取（python）
- `6.4_协程爬虫（asyncio_+_aiohttp）/04.py`：6.4.5 并发限制：Semaphore（python）
- `6.4_协程爬虫（asyncio_+_aiohttp）/05.py`：6.4.6 实战：高并发异步爬取图书网站（python）
## 6.5 三种方案的综合对比与选择

- `6.5_三种方案的综合对比与选择/01.py`：6.4.7 小结（python）
## 6.6 实战：多线程 + 队列的完整爬虫

- `6.6_实战：多线程_+_队列的完整爬虫/01.py`：6.4.7 小结（python）
