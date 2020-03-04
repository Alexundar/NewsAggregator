import logging

from bs4 import BeautifulSoup

from crawler.abstract_crawler import AbstractCrawler


class TutbyCrawler(AbstractCrawler):
    BASE_URL = 'https://news.tut.by/'

    def __init__(self, http_client):
        super().__init__(http_client)
        self.logger = logging.getLogger(TutbyCrawler.__name__)

    def crawl(self):
        with self.http_client:
            self.logger.debug(f'Crawling url #{self.BASE_URL}')
            main_page_status, main_page_content = self.http_client.get(self.BASE_URL, self.HEADERS)
            if main_page_status == 200:
                urls = []
                soup = BeautifulSoup(main_page_content, 'html.parser')
                divs = soup.find_all('div', attrs={'class': 'news-entry'})
                for div in divs:
                    a = div.find('a', attrs={'class': 'entry__link'})
                    urls.append(a['href'])
                for url in urls:
                    self.logger.debug(f'Crawling url #{url}')
                    status, content = self.http_client.get(url, self.HEADERS)
                    if status == 200:
                        yield content, url
                    else:
                        self.logger.warning(f'Request to {url} failed with {content}')
            else:
                self.logger.warning(f'Request to {self.BASE_URL} failed with {main_page_content}')


'''
    def get_urls(self, content):
        urls = []
        soup = BeautifulSoup(content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'news-entry'})
        for div in divs:
            a = div.find('a', attrs={'class': 'entry__link'})
            urls.append(a['href'])
        return urls
        '''
