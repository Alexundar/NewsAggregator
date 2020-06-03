FROM python:3.8-alpine
RUN apk --update add gcc build-base
COPY requirements.txt home/requirements.txt
RUN pip install -r home/requirements.txt
COPY api home/api
COPY client home/client
COPY async_crawler home/async_crawler
COPY async_scraper home/async_scraper
COPY crawler home/crawler
COPY mixins home/mixins
COPY scraper home/scraper
COPY site_parser home/site_parser
COPY storage home/storage
COPY main.py home/main.py
COPY async_main.py home/async_main.py
COPY logging_configuration.json home/logging_configuration.json
WORKDIR /home
ENV PYTHONPATH=/home
ENTRYPOINT ["python", "api/app.py"]