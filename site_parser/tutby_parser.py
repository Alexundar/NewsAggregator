import logging

from bs4 import BeautifulSoup

from site_parser.abstract_parser import AbstractParser


class TutbyPasrser(AbstractParser):
    def __init__(self):
        self.logger = logging.getLogger(TutbyPasrser.__name__)

    def parse(self, content, url):
        news = []
        try:
            soup = BeautifulSoup(content, 'html.parser')
            header = soup.find('div', attrs={'class': 'm_header'}).text
            text = soup.find('div', attrs={'id': 'article_body'}).text
            news.append({
                'URL': url,
                'header': header,
                'text': text,
            })
        except:
            self.logger.debug(f'Problem with HTML code in {url}')
        return news
