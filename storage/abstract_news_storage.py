from abc import ABC, abstractmethod

from mixins import StorageTelemetryMixin


class AbstractNewsStorage(ABC, StorageTelemetryMixin):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def store(self, news):
        pass

    @abstractmethod
    def find(self, site):
        pass
