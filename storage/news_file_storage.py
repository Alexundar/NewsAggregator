import json

from storage.abstract_news_storage import AbstractNewsStorage


class NewsFileStorage(AbstractNewsStorage):
    FILENAME = 'data/{site}_parsed_news.json'

    def __init__(self, site):
        super().__init__()
        self.site = site

    def store(self, news):
        with open(self.FILENAME.format(site=self.site), 'w', encoding="UTF-8") as file:
            json.dump(news, file, sort_keys=True, indent=2, ensure_ascii=False)

    def delete(self):
        raise NotImplementedError()

    def find(self, site):
        raise NotImplementedError()
