# 对应：第10章 分布式爬虫的设计
# 小节：10.3 基于 Redis 手动实现分布式爬虫
# 条目：10.3.3 启动与恢复实验
# 清单：02
# 说明：摘自书稿示例，未改写。

python worker.py init --namespace lesson01 --pages 3
python worker.py worker --namespace lesson01
python worker.py monitor --namespace lesson01
