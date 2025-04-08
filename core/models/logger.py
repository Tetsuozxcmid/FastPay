import logging
import sys


class Logger:
    def __init__(self, name=__name__):
        self.name = name
        self.logger = logging.getLogger(name=self.name)

        self.logger.setLevel(logging.INFO)

        handler = logging.StreamHandler(stream=sys.stdout)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)


logger = Logger()
