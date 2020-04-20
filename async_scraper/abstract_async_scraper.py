from abc import ABC, abstractmethod


class AbstractAsyncScraper(ABC):
    @abstractmethod
    async def async_scrape(self, *args):
        pass
