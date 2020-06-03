import logging

import aiohttp

from client.abstract_async_http_client import AbstractAsyncHTTPClient


class AsyncHTTPClient(AbstractAsyncHTTPClient):
    def __init__(self):
        self.session = None
        self.logger = logging.getLogger(AsyncHTTPClient.__name__)

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()

    async def __aexit__(self, exception_type, exception_value, exception_traceback):
        await super().__aexit__(exception_type, exception_value, exception_traceback)
        await self.session.close()

    async def get(self, url, headers=None):
        self.logger.debug(f'Performing request to {url}')
        async with self.session.get(url, ssl=False, headers=headers) as response:
            return response.status, await response.read()
