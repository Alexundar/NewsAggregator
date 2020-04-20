from bs4 import BeautifulSoup

from crawler.abstract_crawler import AbstractCrawler
from mixins import TutByTelemetryMixin


class TutbyCrawler(AbstractCrawler, TutByTelemetryMixin):
    BASE_URL = 'https://news.tut.by/'

    def __init__(self, http_client):
        super().__init__(http_client)

    def crawl(self, urls):
        with self.http_client:
            for url in urls:
                self.logger.debug(f'Crawling url #{url}')
                status, content = self.http_client.get(url, self.HEADERS)
                if status == 200:
                    yield content, url
                else:
                    self.logger.warning(f'Request to {url} failed with {content}')

    def crawl_urls(self):
        with self.http_client:
            self.logger.debug(f'Crawling url #{self.BASE_URL}')
            main_page_status, main_page_content = self.http_client.get(self.BASE_URL, self.HEADERS)
            if main_page_status == 200:
                soup = BeautifulSoup(main_page_content, 'html.parser')
                news = soup.find_all('div', attrs={'class': 'news-entry'})
                return [
                    article.find('a', attrs={'class': 'entry__link'})['href']
                    for article in news
                ]
            else:
                self.logger.warning(f'Request to {self.BASE_URL} failed with {main_page_content}')
