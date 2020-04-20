import logging


class StorageTelemetryMixin:
    NAME = 'Storage'

    def __init__(self):
        self.logger = logging.getLogger(self.NAME)
