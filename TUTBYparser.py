import json
import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': "*/*",
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
base_url = 'https://news.tut.by/'


def file_writer(news):
    with open('data/tutby_prased_news.json', 'w', encoding="UTF-8") as file:
        json.dump(news, file, sort_keys=True, indent=2)


# парс по каждому урлу
def news_page_parse(urls, headers):
    i = 0
    news = []
    session = requests.Session()
    for url in urls:
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            try:
                soup = bs(request.content, 'html.parser')
                header = soup.find('div', attrs={'class': 'm_header'}).text
                text = soup.find('div', attrs={'id': 'article_body'}).text
                news.append({
                    'URL': url,
                    'header': header,
                    'text': text,
                })
                print(i, ' ', url)  # чтобы посмотреть, что все ок
                i += 1
            except:
                print('url with error: ' + url)
                continue
        else:
            print('Error')
    print(news)
    return news


# парс урлов news.tut.by
def tutby_url_parse(base_url, headers):
    urls = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'news-entry'})
        for div in divs:
            a = div.find('a', attrs={'class': 'entry__link'})
            urls.append(a['href'])
    else:
        print('Error')
    return urls


def main():
    file_writer(news_page_parse(tutby_url_parse(base_url, headers), headers))


if __name__ == '__main__':
    main()
