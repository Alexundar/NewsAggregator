FROM python:3.8-alpine

RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./api ./client ./async_crawler ./async_scraper ./crawler ./data ./logs ./mixins ./scraper ./site_parser ./storage main.py/ logging_configuration.json/

ENTRYPOINT FLASK_APP=/api/app.py flask run