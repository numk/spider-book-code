# 对应：第10章 分布式爬虫的设计
# 小节：10.4 基于 scrapy-redis 的分布式爬虫
# 条目：10.4.2 完整工作节点
# 清单：02
# 说明：摘自书稿示例，未改写。

"""Run identical files on workers with the same Redis URL and crawl name."""
import json
from os import getenv
from urllib.parse import urlparse
import redis
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import DropItem
from scrapy_redis.spiders import RedisSpider


class ResultsPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        obj = cls()
        obj.client = redis.Redis.from_url(crawler.settings["REDIS_URL"], decode_responses=True)
        obj.key = crawler.settings["RESULTS_KEY"]
        crawler.signals.connect(obj.close, signal=signals.spider_closed)
        return obj

    def process_item(self, item, spider=None):
        if not all(item.get(field) for field in ("url", "title", "price")):
            raise DropItem("书籍字段缺失")
        # URL 是稳定标识；重复下载覆盖相同记录，不能累加为新书籍。
        self.client.hset(self.key, item["url"], json.dumps(dict(item), ensure_ascii=False))
        return item

    def close(self, spider=None, reason=None):
        self.client.close()


class BookSpider(RedisSpider):
    name = getenv("CRAWL_NAME", "books_lesson")
    redis_key = name + ":start_urls"
    allowed_domains = ["books.toscrape.com"]

    def parse(self, response):
        for card in response.css("article.product_pod"):
            href = card.css("h3 a::attr(href)").get()
            yield {"url": response.urljoin(href) if href else None,
                   "title": card.css("h3 a::attr(title)").get(),
                   "price": card.css(".price_color::text").get()}
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            target = response.urljoin(next_page)
            path = urlparse(target).path
            page = int(path.rsplit("page-", 1)[-1].split(".")[0])
            if page <= int(getenv("MAX_PAGES", "3")):
                yield response.follow(target, self.parse)


if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "REDIS_URL": getenv("REDIS_URL", "redis://localhost:6379/0"),
        "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
        "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",
        "SCHEDULER_PERSIST": True,
        "ITEM_PIPELINES": {ResultsPipeline: 300},
        "RESULTS_KEY": BookSpider.name + ":results",
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "DOWNLOAD_DELAY": 1,
        "DOWNLOAD_TIMEOUT": 20,
        "RETRY_TIMES": 2,
        "LOG_LEVEL": "INFO",
    })
    process.crawl(BookSpider)
    process.start()
