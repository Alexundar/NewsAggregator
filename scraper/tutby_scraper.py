from crawler import TutbyCrawler
from scraper.abstract_scraper import AbstractScraper
from site_parser import TutbyParser


class TutByScraper(AbstractScraper):
    def __init__(self, http_client):
        self.crawler = TutbyCrawler(http_client)
        self.parser = TutbyParser()

    def scrape(self, site):
        news = []
        urls = self.crawler.crawl_urls()
        for content, url in self.crawler.crawl(urls):
            news.extend(self.parser.parse(content, url, site))
        return news
