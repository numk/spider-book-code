# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.3 JavaScript 逆向教学实战
# 清单：12
# 说明：摘自书稿示例，未改写。

"""Local signature classroom; the public salt is not authentication."""
import hashlib
import hmac
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

BASE = Path(__file__).resolve().parent


def sign(keyword, page, timestamp):
    raw = json.dumps([keyword, page, timestamp, "classroom-salt"],
                     ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, message, *args):
        print(message % args)

    def reply(self, status, data, content_type="application/json; charset=utf-8"):
        body = data if isinstance(data, bytes) else json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlsplit(self.path)
        assets = {"/": ("index.html", "text/html; charset=utf-8"),
                  "/sign.mjs": ("sign.mjs", "text/javascript; charset=utf-8")}
        if url.path in assets:
            name, mime = assets[url.path]
            return self.reply(200, (BASE / name).read_bytes(), mime)
        if url.path != "/api/search":
            return self.reply(404, {"error": "not found"})
        try:
            values = parse_qs(url.query, keep_blank_values=True)
            if any(len(values.get(key, [])) != 1 for key in ("keyword", "page", "timestamp", "sign")):
                raise ValueError("参数缺失或重复")
            keyword = values["keyword"][0]
            page, timestamp = int(values["page"][0]), int(values["timestamp"][0])
            if not keyword or not 1 <= page <= 10:
                raise ValueError("关键词或页码无效")
        except (KeyError, ValueError) as error:
            return self.reply(400, {"error": str(error)})
        if abs(time.time() - timestamp) > 300:
            return self.reply(403, {"error": "timestamp expired"})
        if not hmac.compare_digest(values["sign"][0], sign(keyword, page, timestamp)):
            return self.reply(403, {"error": "signature mismatch"})
        self.reply(200, {"items": [{"title": keyword, "page": page}]})


if __name__ == "__main__":
    print("打开 http://127.0.0.1:8765")
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
