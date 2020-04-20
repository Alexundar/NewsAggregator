from async_crawler import TutbyAsyncCrawler
from crawler import TutbyCrawler
from async_scraper.abstract_async_scraper import AbstractAsyncScraper
from site_parser import TutbyParser
from client import HTTPClient


class TutByAsyncScraper(AbstractAsyncScraper):
    def __init__(self, async_http_client):
        self.http_client = HTTPClient()
        self.async_crawler = TutbyAsyncCrawler(async_http_client)
        self.crawler = TutbyCrawler(self.http_client)
        self.parser = TutbyParser()

    async def async_scrape(self, site):
        urls = self.crawler.crawl_urls()
        news = []
        for content, url in zip(await self.async_crawler.async_crawl(urls), urls):
            news.extend(self.parser.parse(content, url,  site))
        return news
