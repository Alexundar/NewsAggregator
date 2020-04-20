import logging

from bs4 import BeautifulSoup

from site_parser.abstract_parser import AbstractParser


class TutbyParser(AbstractParser):
    def __init__(self):
        self.logger = logging.getLogger(TutbyParser.__name__)

    def parse(self, content, url, site):
        news = []
        try:
            soup = BeautifulSoup(content, 'html.parser')
            header_block = soup.find('div', attrs={'class': 'm_header'})
            article_block = soup.find('div', attrs={'id': 'article_body'})
            if header_block and article_block:
                news.append({
                    'site_name': site,
                    'URL': url,
                    'header': header_block.text,
                    'text': article_block.text,
                })
        except Exception as exception:
            self.logger.warning(f'Problem with HTML code in {url}: {exception}')
        return news
