import logging

import requests

from client.abstract_http_client import AbstractHTTPClient


class HTTPClient(AbstractHTTPClient):
    def __init__(self):
        self.session = None
        self.logger = logging.getLogger(HTTPClient.__name__)

    def __enter__(self):
        self.session = requests.Session()

    def __exit__(self, exception_type, exception_value, exception_traceback):
        super().__exit__(exception_type, exception_value, exception_traceback)
        self.session.close()

    def get(self, url, headers=None):
        self.logger.debug(f'Performing request to {url}')
        response = self.session.get(url, headers=headers)
        return response.status_code, response.content
