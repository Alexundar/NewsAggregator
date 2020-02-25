import json
import requests
from bs4 import BeautifulSoup as bs
import IParser


class NavinyByParser(object, IParser):
    __headers = {'accept': "*/*",
                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                               '(KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
    __base_url = 'https://naviny.by/archive/news?page='

    @staticmethod
    def file_writer(self, news):
        with open('data/naviny_by_prased_news.json', 'w', encoding="UTF-8") as __file:
            json.dump(news, __file, sort_keys=True, indent=2)

    @staticmethod
    def naviny_by_parse(self):
        __news = []
        __session = requests.Session()
        for i in range(5):
            __request = __session.get(self._base_url + str(i), headers=self._headers)
            if __request.status_code == 200:
                __soup = bs(__request.content, 'html.parser')
                __articles = __soup.find_all('div', attrs={'class': 'media'})
                for article in __articles:
                    __header = article.find('h3', attrs={'class': 'media-heading'})
                    try:
                        __url = __header.find('a')['href']
                        __text = article.find('p').text
                        __news.append({
                            'URL': __url,
                            'header': __header.text,
                            'text': __text
                        })
                    except:
                        print('error')
            else:
                print('Error')
        return __news
