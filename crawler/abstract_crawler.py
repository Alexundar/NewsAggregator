from abc import ABC, abstractmethod


class AbstractCrawler(ABC):
    HEADERS = {'accept': "*/*",
               'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client

    @abstractmethod
    def crawl(self, *args):
        pass
