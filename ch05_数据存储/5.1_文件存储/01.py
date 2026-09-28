# 对应：第5章 数据存储
# 小节：5.1 文件存储
# 条目：5.1.1 TXT 文件的存储
# 清单：01
# 说明：摘自书稿示例，未改写。

from pathlib import Path

path = Path("data.txt")
path.write_text("Python 爬虫实战\n", encoding="utf-8")
with path.open("a", encoding="utf-8") as stream:
    stream.write("Python 数据分析\n")
print(path.read_text(encoding="utf-8"))
