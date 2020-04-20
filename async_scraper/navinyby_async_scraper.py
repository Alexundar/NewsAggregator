from async_crawler import NavinybyAsyncCrawler
from async_scraper.abstract_async_scraper import AbstractAsyncScraper
from site_parser import NavinyByParser


class NavinybyAsyncScraper(AbstractAsyncScraper):
    NUMBER_OF_PAGES = 5

    def __init__(self, http_client):
        self.async_crawler = NavinybyAsyncCrawler(http_client)
        self.parser = NavinyByParser()

    async def async_scrape(self, site):
        news = []
        for content in await self.async_crawler.async_crawl(self.NUMBER_OF_PAGES):
            news.extend(self.parser.parse(content, site))
        return news
