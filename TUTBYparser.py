import json
import requests
from bs4 import BeautifulSoup as bs
import IParser


class TutByPasrser(object, IParser):
    __headers = {'accept': "*/*",
                 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36'
                               ' (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    __base_url = 'https://news.tut.by/'

    @staticmethod
    def file_writer(self, news):
        with open('data/tutby_prased_news.json', 'w', encoding="UTF-8") as __file:
            json.dump(news, __file, sort_keys=True, indent=2)

    @staticmethod
    def news_page_parse(self, urls):
        __news = []
        __session = requests.Session()
        for url in urls:
            __request = __session.get(url, headers=self.__headers)
            if __request.status_code == 200:
                try:
                    __soup = bs(__request.content, 'html.parser')
                    __header = __soup.find('div', attrs={'class': 'm_header'}).text
                    __text = __soup.find('div', attrs={'id': 'article_body'}).text
                    __news.append({
                        'URL': url,
                        'header': __header,
                        'text': __text,
                    })
                except:
                    print('url with error: ' + url)
                    continue
            else:
                print('Error')
        return __news

    @staticmethod
    def tutby_url_parse(self):
        __urls = []
        __session = requests.Session()
        __request = __session.get(self.__base_url, headers=self.__headers)
        if __request.status_code == 200:
            __soup = bs(__request.content, 'html.parser')
            __divs = __soup.find_all('div', attrs={'class': 'news-entry'})
            for div in __divs:
                __a = div.find('a', attrs={'class': 'entry__link'})
                __urls.append(__a['href'])
        else:
            print('Error')
        return __urls
