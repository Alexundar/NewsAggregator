from crawler import HrodnaLifeCrawler
from scraper.abstract_scraper import AbstractScraper
from site_parser import HrodnaLifeParser


class HrodnaLifeScraper(AbstractScraper):
    NUMBER_OF_PAGES = 5

    def __init__(self, http_client):
        self.crawler = HrodnaLifeCrawler(http_client)
        self.parser = HrodnaLifeParser()

    def scrape(self, site):
        news = []
        for content in self.crawler.crawl(self.NUMBER_OF_PAGES):
            news.extend(self.parser.parse(content, site))
        return news
