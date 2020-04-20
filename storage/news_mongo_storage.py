import pymongo

from storage.abstract_news_storage import AbstractNewsStorage


class NewsMongoStorage(AbstractNewsStorage):
    DATABASE_NAME = 'news_aggregator'
    COLLECTION_NAME = 'news'

    def __init__(self):
        super().__init__()
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client[self.DATABASE_NAME]
        self.news_collection = self.database[self.COLLECTION_NAME]

    def store(self, news):
        self.logger.info(f'Inserting {len(news)} news into database')
        self.news_collection.insert_many(news)

    def find(self, site=None):
        if site:
            return self.__find_by_query({'site_name': site})
        else:
            return self.__find_all()

    def __find_by_query(self, query):
        yield from self.news_collection.find(query)

    def __find_all(self):
        yield from self.news_collection.find()
