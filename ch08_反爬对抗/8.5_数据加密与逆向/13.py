# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.3 JavaScript 逆向教学实战
# 清单：13
# 说明：摘自书稿示例，未改写。

import json
import subprocess
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
from server import sign


def javascript_sign(keyword, page, timestamp):
    result = subprocess.run(
        ["node", str(Path(__file__).with_name("sign.mjs")),
         json.dumps([keyword, page, timestamp], ensure_ascii=False)],
        check=True, capture_output=True, text=True, encoding="utf-8", timeout=10)
    return result.stdout.strip()


if __name__ == "__main__":
    values = ("Python爬虫", 1, int(time.time()))
    python_result = sign(*values)
    assert python_result == javascript_sign(*values)
    query = urlencode(dict(zip(("keyword", "page", "timestamp"), values)) | {"sign": python_result})
    with urlopen("http://127.0.0.1:8765/api/search?" + query, timeout=10) as response:
        print(json.loads(response.read()))
