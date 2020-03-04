import json


class NewsFileStorage:
    FILENAME = 'data/{site}_parsed_news.json'

    def __init__(self, site):
        self.site = site

    def store(self, news):
        with open(self.FILENAME.format(site=self.site), 'w', encoding="UTF-8") as file:
            json.dump(news, file, sort_keys=True, indent=2, ensure_ascii=False)
