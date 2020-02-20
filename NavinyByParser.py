import json
import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': "*/*",
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
base_url = 'https://naviny.by/archive/news?page='


def file_writer(news):
    with open('data/naviny_by_prased_news.json', 'w', encoding="UTF-8") as file:
        json.dump(news, file, sort_keys=True, indent=2)


def naviny_by_parse(base_url, headers):
    news = []
    session = requests.Session()
    for i in range(5):
        request = session.get(base_url + str(i), headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            articles = soup.find_all('div', attrs={'class': 'media'})
            for article in articles:
                header = article.find('h3', attrs={'class': 'media-heading'})
                try:
                    url = header.find('a')['href']
                    text = article.find('p').text
                    news.append({
                        'URL': url,
                        'header': header.text,
                        'text': text
                    })
                except:
                    print('error')
        else:
            print('Error')
    return news


def main():
    # file_writer(news_page_parse(tutby_url_parse(base_url, headers), headers))
    print(naviny_by_parse(base_url, headers))
    file_writer(naviny_by_parse(base_url, headers))


if __name__ == '__main__':
    main()
