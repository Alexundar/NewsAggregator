from crawler import NavinybyCrawler
from scraper.abstract_scraper import AbstractScraper
from site_parser import NavinyByParser


class NavinybyScraper(AbstractScraper):
    NUMBER_OF_PAGES = 5

    def __init__(self, http_client):
        self.crawler = NavinybyCrawler(http_client)
        self.parser = NavinyByParser()

    def scrape(self, site):
        news = []
        for content in self.crawler.crawl(self.NUMBER_OF_PAGES):
            news.extend(self.parser.parse(content, site))
        return news
