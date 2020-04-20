import logging

from bs4 import BeautifulSoup

from site_parser.abstract_parser import AbstractParser


class HrodnaLifeParser(AbstractParser):
    def __init__(self):
        self.logger = logging.getLogger(HrodnaLifeParser.__name__)

    def parse(self, content, site):
        news = []
        soup = BeautifulSoup(content, 'html.parser')
        articles = soup.find_all('article', attrs={'class': 'list-post'})
        self.logger.debug(f'Found {len(articles)} articles')
        for article in articles:
            header = article.find('h2', attrs={'class': 'post-title'})
            url = header.find('a')['href']
            text = article.find('p').text
            news.append({
                'site_name': site,
                'URL': url,
                'header': header.text,
                'text': text
            })
        return news
