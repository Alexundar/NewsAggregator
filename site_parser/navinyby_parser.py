import logging

from bs4 import BeautifulSoup

from site_parser.abstract_parser import AbstractParser


class NavinyByParser(AbstractParser):
    def __init__(self):
        self.logger = logging.getLogger(NavinyByParser.__name__)

    def parse(self, content, site):
        news = []
        soup = BeautifulSoup(content, 'html.parser')
        articles = soup.find_all('div', attrs={'class': 'media'})
        self.logger.debug(f'Found {len(articles)} articles')
        for article in articles:
            header = article.find('h3', attrs={'class': 'media-heading'})
            try:
                url = header.find('a')['href']
                text = article.find('p').text
                news.append({
                    'site_name': site,
                    'URL': url,
                    'header': header.text,
                    'text': text
                })
            except Exception as exception:
                self.logger.warning(f'Problem with HTML code in {url}: {exception}')
        return news
