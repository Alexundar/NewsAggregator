from async_crawler import HrodnaLifeAsyncCrawler
from async_scraper.abstract_async_scraper import AbstractAsyncScraper
from site_parser import HrodnaLifeParser


class HrodnaLifeAsyncScraper(AbstractAsyncScraper):
    NUMBER_OF_PAGES = 5

    def __init__(self, http_client):
        self.async_crawler = HrodnaLifeAsyncCrawler(http_client)
        self.parser = HrodnaLifeParser()

    async def async_scrape(self, site):
        news = []
        for content in await self.async_crawler.async_crawl(self.NUMBER_OF_PAGES):
            news.extend(self.parser.parse(content, site))
        return news
