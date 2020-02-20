import json
import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': "*/*",
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
base_url = 'https://ru.hrodna.life/novosti/page/'


def file_writer(news):
    with open('data/hrodna_life_prased_news.json', 'w', encoding="UTF-8") as file:
        json.dump(news, file, sort_keys=True, indent=2)


def hrodna_life_parse(base_url, headers):
    news = []
    session = requests.Session()
    for i in range(10):
        request = session.get(base_url+str(i), headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            articles = soup.find_all('article', attrs={'class': 'list-post'})
            for article in articles:
                header = article.find('h2', attrs={'class': 'post-title'})
                url = header.find('a')['href']
                text = article.find('p').text
                news.append({
                    'URL': url,
                    'header': header.text,
                    'text': text
                })
        else:
            print('Error')

    return news


def main():
    # file_writer(news_page_parse(tutby_url_parse(base_url, headers), headers))
    print(hrodna_life_parse(base_url, headers))
    file_writer(hrodna_life_parse(base_url, headers))


if __name__ == '__main__':
    main()
