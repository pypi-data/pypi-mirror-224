#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import colorlog
from pitrix.constants.constants import LogConfig

class Log:

    def __init__(self, name=None, log_level=LogConfig.DEFAULT_LOG_LEVEL):
        self.logger = logging.getLogger(name)

        self.logger.setLevel(log_level)

        console_formatter = colorlog.ColoredFormatter(fmt=LogConfig.CONSOLE_FMT, log_colors=LogConfig.COLOR)
        file_formatter = logging.Formatter(fmt=LogConfig.CONSOLE_FMT)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(log_level)

        if name:
            file_handler = logging.FileHandler(filename=name, mode='a', encoding='utf-8')
            file_handler.setFormatter(file_formatter)
            file_handler.setLevel(logging.ERROR)

        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
            if name:
                self.logger.addHandler(file_handler)

    def debug(self, message, *args, **kwargs):
        self.logger.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.logger.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self.logger.critical(message, *args, **kwargs)

log = Log()

if __name__ == '__main__':
    log.info('nihao')