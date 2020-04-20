from abc import ABC, abstractmethod


class AbstractAsyncHTTPClient(ABC):
    async def __aenter__(self):
        pass

    async def __aexit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:
            raise

    @abstractmethod
    async def get(self, url, headers=None):
        pass
