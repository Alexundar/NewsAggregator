import json
import requests
from bs4 import BeautifulSoup as bs
import IParser


class HrodnaLifeParser(object, IParser):
    __headers = {'accept': "*/*",
                 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36'
                               ' (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    __base_url = 'https://ru.hrodna.life/novosti/page/'

    @staticmethod
    def file_writer(news):
        with open('data/hrodna_life_prased_news.json', 'w', encoding="UTF-8") as __file:
            json.dump(news, __file, sort_keys=True, indent=2)

    @staticmethod
    def hrodna_life_parse(self):
        __news = []
        __session = requests.Session()
        for i in range(10):
            __request = __session.get(self.__base_url + str(i), headers=self.__headers)
            if __request.status_code == 200:
                __soup = bs(__request.content, 'html.parser')
                __articles = __soup.find_all('article', attrs={'class': 'list-post'})
                for article in __articles:
                    __header = article.find('h2', attrs={'class': 'post-title'})
                    __url = __header.find('a')['href']
                    __text = article.find('p').text
                    __news.append({
                        'URL': __url,
                        'header': __header.text,
                        'text': __text
                    })
            else:
                print('Error')

        return __news
