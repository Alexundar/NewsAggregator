from abc import ABC, abstractmethod


class AbstractScraper(ABC):
    @abstractmethod
    def scrape(self, *args):
        pass
