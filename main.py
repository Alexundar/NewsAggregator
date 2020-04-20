import json
import logging.config

from client import HTTPClient
from scraper import NavinybyScraper, TutByScraper, HrodnaLifeScraper
from storage import NewsFileStorage, NewsMongoStorage

SCRAPERS = {
    'hrodna_life': HrodnaLifeScraper,
    'tutby': TutByScraper,
    'navinyby': NavinybyScraper
}


def read_logging_configuration():
    with open('logging_configuration.json') as file:
        return json.loads(file.read())


if __name__ == '__main__':
    logging.config.dictConfig(read_logging_configuration())
    client = HTTPClient()
    db = NewsMongoStorage()
    for site, Scraper in SCRAPERS.items():
        scraper = Scraper(client)
        news = scraper.scrape(site)
        storage = NewsFileStorage(site)
        storage.store(news)
        db.store(news)
