import logging


class NavinyByTelemetryMixin:
    NAME = 'NavinyBy'

    def __init__(self):
        self.logger = logging.getLogger(self.NAME)
