from crawler import TutbyCrawler
from scraper.abstract_scraper import AbstractScraper
from site_parser import TutbyPasrser


class TutByScraper(AbstractScraper):
    def __init__(self, http_client):
        self.crawler = TutbyCrawler(http_client)
        self.parser = TutbyPasrser()

    def scrape(self):
        news = []
        crawled = self.crawler.crawl()
        for content, url in crawled:
            news.extend(self.parser.parse(content, url))
        return news
