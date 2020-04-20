import asyncio

from async_crawler.abstract_async_crawler import AbstractAsyncCrawler
from mixins import TutByTelemetryMixin


class TutbyAsyncCrawler(AbstractAsyncCrawler, TutByTelemetryMixin):
    BASE_URL = 'https://news.tut.by/'

    def __init__(self, http_client):
        super().__init__(http_client)

    async def async_crawl(self, urls):
        news_content = []
        async with self.http_client:
            requests = []
            for url in urls:
                self.logger.debug(f'Crawling url #{url}')
                requests.append(self.http_client.get(url, self.HEADERS))
            for request in asyncio.as_completed(requests):
                status, content = await request
                if status == 200:
                    news_content.append(content)
                else:
                    self.logger.warning(f'Request to {url} failed with {content}')
        return news_content
