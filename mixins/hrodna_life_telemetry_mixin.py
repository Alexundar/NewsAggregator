import logging


class HrodnaLifeTelemetryMixin:
    NAME = 'HrodnaLife'

    def __init__(self):
        self.logger = logging.getLogger(self.NAME)
