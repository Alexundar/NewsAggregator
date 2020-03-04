import logging

from crawler.abstract_crawler import AbstractCrawler


class NavinybyCrawler(AbstractCrawler):
    BASE_URL = 'https://naviny.by/archive/news?page={page}'

    def __init__(self, http_client):
        super().__init__(http_client)
        self.logger = logging.getLogger(NavinybyCrawler.__name__)

    def crawl(self, number_of_pages):
        with self.http_client:
            for page in range(number_of_pages):
                url = self.BASE_URL.format(page=page)
                self.logger.debug(f'Crawling page #{page}')
                status, content = self.http_client.get(url, self.HEADERS)
                if status == 200:
                    yield content
                else:
                    self.logger.warning(f'Request to {url} failed with {status}')
