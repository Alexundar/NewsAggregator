import json

from flask import Flask

from storage import NewsMongoStorage

app = Flask(__name__)

db = NewsMongoStorage()


def convert_to_dto(news):
    return [
        {
            'site_name': article['site_name'],
            'url': article['URL'],
            'header': article['header'],
            'text': article['text']
        }
        for article in news
    ]


@app.route('/news')
def get_all_news():
    news = convert_to_dto(db.find())
    if news:
        return json.dumps(news, ensure_ascii=False)
    else:
        return 'Not found', 404


@app.route('/news/<site>')
def get_news_by_site(site):
    '''

    :param site:
    :return:
    '''
    news = convert_to_dto(db.find(site))
    if news:
        return json.dumps(news, ensure_ascii=False)
    else:
        return 'Not found', 404


if __name__ == '__name__':
    app.run(debug=True)
