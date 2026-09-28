# 对应：第9章 Scrapy 框架的使用
# 小节：9.7 Middleware：中间件
# 条目：9.7.2 代理与有限重试
# 清单：02
# 说明：摘自书稿示例，未改写。

import asyncio
import random
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from scrapy.downloadermiddlewares.retry import get_retry_request

class ProxyMiddleware:
    PROXIES = []  # 填入经过验证的代理地址；为空时直接连接

    def process_request(self, request, spider):
        if self.PROXIES:
            request.meta['proxy'] = random.choice(self.PROXIES)

    async def process_response(self, request, response, spider):
        if response.status not in (403, 429):
            return response
        retry = get_retry_request(request, spider=spider, reason=response.status,
                                  max_retry_times=2)
        if retry is None:
            return response
        attempt = retry.meta['retry_times']
        delay = min(2 ** attempt, 30)
        retry_after = response.headers.get('Retry-After', b'')
        if retry_after.isdigit():
            delay = max(delay, int(retry_after))
        elif retry_after:
            try:
                until = parsedate_to_datetime(retry_after.decode('ascii'))
                if until.tzinfo is None:
                    until = until.replace(tzinfo=timezone.utc)
                delay = max(delay, (until - datetime.now(timezone.utc)).total_seconds())
            except (ValueError, TypeError, UnicodeError):
                return response  # 无法解释服务端等待要求，交给调用方记录检查
        if delay > 60:
            spider.logger.warning('服务端要求较长等待，暂停自动重试')
            return response
        await asyncio.sleep(delay)
        return retry
