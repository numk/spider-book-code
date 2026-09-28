# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.12 iOS 数据分析入门
# 条目：12.12.2 从操作定位到请求复现
# 清单：01
# 说明：摘自书稿示例，未改写。

import requests

payload = {"keyword": "Python", "page": 1, "page_size": 20}
with requests.Session() as session:
    response = session.post(
        "https://httpbin.org/anything",
        json=payload,
        headers={"Accept": "application/json"},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    assert data["json"] == payload
    print("回显验证成功：{}".format(data["json"]))
