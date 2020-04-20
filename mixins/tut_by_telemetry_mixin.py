import logging


class TutByTelemetryMixin:
    NAME = 'TutBy'

    def __init__(self):
        self.logger = logging.getLogger(self.NAME)
