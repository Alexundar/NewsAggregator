import asyncio
import json
import logging.config
import os
import threading

from async_scraper import HrodnaLifeAsyncScraper, TutByAsyncScraper, NavinybyAsyncScraper
from client import AsyncHTTPClient
from storage import NewsMongoStorage

SCRAPERS = {
    'hrodna_life': HrodnaLifeAsyncScraper,
    'tutby': TutByAsyncScraper,
    'navinyby': NavinybyAsyncScraper
}

os.environ['SCRAPER'] = 'SEQ'


def read_logging_configuration():
    with open('logging_configuration.json') as file:
        return json.loads(file.read())


async def async_scrape(db, async_http_client, news):
    db.delete()
    for site, Scraper in SCRAPERS.items():
        scraper = Scraper(async_http_client)
        news.append(scraper.async_scrape(site))
    for article in asyncio.as_completed(news):
        db.store(await article)


async def seq_scrape(db, async_http_client, news):
    db.delete()
    for site, Scraper in SCRAPERS.items():
        scraper = Scraper(async_http_client)
        news.append(await scraper.async_scrape(site))
    for article in news:
        db.store(article)


async def async_main():
    threading.Timer(10 * 3600, async_main).start()
    logging.config.dictConfig(read_logging_configuration())
    async_http_client = AsyncHTTPClient()
    db = NewsMongoStorage()
    news = []
    if os.environ.get('SCRAPER') == 'SEQ':
        await seq_scrape(db, async_http_client, news)
    elif os.environ.get('SCRAPER') == 'ASYNC':
        await async_scrape(db, async_http_client, news)


if __name__ == '__main__':
    asyncio.run(async_main())
