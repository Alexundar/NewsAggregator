from abc import abstractmethod


class AbstractParser:
    @abstractmethod
    def parse(self, *args):
        pass
