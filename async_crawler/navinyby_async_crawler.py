import asyncio

from async_crawler.abstract_async_crawler import AbstractAsyncCrawler
from mixins import NavinyByTelemetryMixin


class NavinybyAsyncCrawler(AbstractAsyncCrawler, NavinyByTelemetryMixin):
    BASE_URL = 'https://naviny.by/archive/news?page={page}'

    def __init__(self, http_client):
        super().__init__(http_client)

    async def async_crawl(self, number_of_pages):
        news_content = []
        async with self.http_client:
            requests = []
            for page in range(number_of_pages):
                url = self.BASE_URL.format(page=page)
                self.logger.debug(f'Crawling page #{page}')
                requests.append(self.http_client.get(url, self.HEADERS))
            for request in asyncio.as_completed(requests):
                status, content = await request
                if status == 200:
                    news_content.append(content)
                else:
                    self.logger.warning(f'Request to {url} failed with {status}')
        return news_content
