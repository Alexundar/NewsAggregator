import logging

from client import HTTPClient
from scraper import HrodnaLifeScraper, TutByScraper, NavinybyScraper
from storage import NewsFileStorage

if __name__ == '__main__':
    logging.basicConfig(filename='logs/hr_life_parser.log', level=logging.DEBUG)
    client = HTTPClient()
    scraper = HrodnaLifeScraper(client)
    news = scraper.scrape()
    storage = NewsFileStorage('hrodna_life')
    storage.store(news)
    logging.basicConfig(filename='logs/tutby_parser.log', level=logging.DEBUG)
    client = HTTPClient()
    scraper = TutByScraper(client)
    news = scraper.scrape()
    storage = NewsFileStorage('tutby')
    storage.store(news)
    logging.basicConfig(filename='logs/naviny_parser.log', level=logging.DEBUG)
    client = HTTPClient()
    scraper = NavinybyScraper(client)
    news = scraper.scrape()
    storage = NewsFileStorage('navinyby')
    storage.store(news)
