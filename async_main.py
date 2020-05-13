import asyncio
import json
import logging.config

from async_scraper import HrodnaLifeAsyncScraper, TutByAsyncScraper, NavinybyAsyncScraper
from client import AsyncHTTPClient
from storage import NewsMongoStorage

SCRAPERS = {
    'hrodna_life': HrodnaLifeAsyncScraper,
    'tutby': TutByAsyncScraper,
    'navinyby': NavinybyAsyncScraper
}


def read_logging_configuration():
    with open('logging_configuration.json') as file:
        return json.loads(file.read())


async def async_main():
    logging.config.dictConfig(read_logging_configuration())
    async_http_client = AsyncHTTPClient()
    db = NewsMongoStorage()
    news = []
    for site, Scraper in SCRAPERS.items():
        scraper = Scraper(async_http_client)
        news.append(scraper.async_scrape(site))
    news = asyncio.as_completed(news)
    for piece_of_news in news:
        db.store(await piece_of_news)


if __name__ == '__main__':
    asyncio.run(async_main())
