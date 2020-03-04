from abc import ABC, abstractmethod


class AbstractHTTPClient(ABC):
    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:
            raise

    @abstractmethod
    def get(self, url, headers=None):
        pass
