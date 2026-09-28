# 对应：第10章 分布式爬虫的设计
# 小节：10.3 基于 Redis 手动实现分布式爬虫
# 条目：10.3.2 完整工作节点
# 清单：01
# 说明：摘自书稿示例，未改写。

"""Redis 7+ classroom queue. Use a fresh namespace for each crawl."""
import argparse
import json
import time
from urllib.parse import urljoin, urlsplit
from uuid import uuid4
import redis
import requests
from bs4 import BeautifulSoup

# All keys share a cluster hash tag. Enqueue intentionally remains two commands.
TRANSITION = """
local pending, leases, owners, attempts, done, failed, results = unpack(KEYS)
local now = tonumber(redis.call('TIME')[1])
local mode, token = ARGV[1], ARGV[2]
if mode == 'claim' then
  local url = redis.call('RPOP', pending)
  if not url then return nil end
  local attempt = redis.call('HINCRBY', attempts, url, 1)
  redis.call('HSET', owners, url, token)
  redis.call('ZADD', leases, now + tonumber(ARGV[3]), url)
  return {url, tostring(attempt)}
end
if mode == 'reclaim' then
  local expired = redis.call('ZRANGEBYSCORE', leases, '-inf', now, 'LIMIT', 0, 100)
  for _, url in ipairs(expired) do
    redis.call('ZREM', leases, url)
    redis.call('HDEL', owners, url)
    if tonumber(redis.call('HGET', attempts, url)) < tonumber(ARGV[3]) then
      redis.call('LPUSH', pending, url)
    else
      redis.call('HSET', failed, url, 'lease expired')
    end
  end
  return #expired
end
local url = ARGV[3]
if redis.call('HGET', owners, url) ~= token then return 0 end
if tonumber(redis.call('ZSCORE', leases, url) or '0') <= now then return 0 end
redis.call('ZREM', leases, url)
redis.call('HDEL', owners, url)
if mode == 'success' then
  local items = cjson.decode(ARGV[4])
  for _, item in ipairs(items) do
    redis.call('HSET', results, item.url, cjson.encode(item))
  end
  redis.call('SADD', done, url)
elseif tonumber(redis.call('HGET', attempts, url)) < tonumber(ARGV[5]) then
  redis.call('LPUSH', pending, url)
else
  redis.call('HSET', failed, url, ARGV[4])
end
return 1
"""


class Queue:
    def __init__(self, client, namespace="lesson", lease=60, max_attempts=3):
        self.r, self.lease, self.max_attempts = client, lease, max_attempts
        prefix = "{" + namespace + "}:"
        self.keys = [prefix + name for name in
                     ("pending", "leases", "owners", "attempts", "success", "failed", "results")]
        self.seen = prefix + "seen"
        self.transition = client.register_script(TRANSITION)

    def push_url(self, url):
        if self.r.sadd(self.seen, url):
            self.r.lpush(self.keys[0], url)
            return True
        return False

    def pop_url(self):
        token = uuid4().hex
        value = self.transition(keys=self.keys, args=["claim", token, self.lease])
        return (value[0], int(value[1]), token) if value else None

    def finish(self, url, token, items=None, error=""):
        mode = "success" if items is not None else "failure"
        payload = json.dumps(items, ensure_ascii=False) if items is not None else error
        return bool(self.transition(keys=self.keys,
                    args=[mode, token, url, payload, self.max_attempts]))

    def reclaim(self):
        return self.transition(keys=self.keys, args=["reclaim", "", self.max_attempts])

    def monitor(self):
        with self.r.pipeline(transaction=True) as pipe:
            pipe.scard(self.seen).llen(self.keys[0]).zcard(self.keys[1])
            pipe.scard(self.keys[4]).hlen(self.keys[5]).hlen(self.keys[6])
            return dict(zip(("seen", "pending", "processing", "success", "failed", "books"), pipe.execute()))


def parse(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    items = []
    for article in soup.select("article.product_pod"):
        link, price = article.select_one("h3 a"), article.select_one(".price_color")
        if link is None or price is None or not link.get("href") or not link.get("title"):
            raise ValueError("列表字段缺失，保留任务供重试或检查")
        items.append(dict(url=urljoin(base_url, link["href"]), title=link["title"], price=price.get_text(strip=True)))
    if not items:
        raise ValueError("没有书籍，不能标记采集成功")
    return items


def worker(queue):
    with requests.Session() as session:
        while True:
            queue.reclaim()
            job = queue.pop_url()
            if job is None:
                print(queue.monitor())
                time.sleep(2)
                continue
            url, attempt, token = job
            try:
                response = session.get(url, timeout=(5, 15))
                response.raise_for_status()
                response.encoding = "utf-8"
                items = parse(response.text, url)
                if not queue.finish(url, token, items=items):
                    print("租约过期或任务已重新分配，放弃旧结果")
            except (requests.RequestException, ValueError) as error:
                time.sleep(min(2 ** attempt, 8))
                queue.finish(url, token, error=str(error))
            print(queue.monitor())
            time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["init", "worker", "monitor"])
    parser.add_argument("--redis", default="redis://localhost:6379/0")
    parser.add_argument("--namespace", default="lesson")
    parser.add_argument("--pages", type=int, default=3)
    args = parser.parse_args()
    queue = Queue(redis.Redis.from_url(args.redis, decode_responses=True), args.namespace)
    if args.mode == "init":
        if not 1 <= args.pages <= 50:
            parser.error("pages 应为 1 到 50")
        for page in range(1, args.pages + 1):
            queue.push_url(f"https://books.toscrape.com/catalogue/page-{page}.html")
        print(queue.monitor())
    elif args.mode == "monitor":
        print(queue.monitor())
    else:
        worker(queue)
