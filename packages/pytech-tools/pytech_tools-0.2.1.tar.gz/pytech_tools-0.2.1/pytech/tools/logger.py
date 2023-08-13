import datetime
import logging

from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

__all__ = [
    "LoggerHandler",
]


class AbstractFormatter(logging.Formatter):
    """
    Abstract Formatter for log messages
    """

    msg_format = " - ".join([
        "%(name)s", "%(asctime)s", "%(levelname)s", "%(message)s",
    ])

    level_formats_keys = (
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    )
    level_formats_values = None

    def set_formats(self):
        """
        Method that needs to be implemented in concrete child classes.

        It needs to overwrite the self.level_formats_values with an interable
        of log formatted strings.
        """
        raise NotImplementedError(
            "set_formats method needs to be implemented"
        )

    def get_formats(self) -> dict:
        """
        Method that executes the self.set_formats if 
        self.leve_formats_values == None

        :return: the formats dict
        k == log_level
        v == log_level formatting
        """
        if not self.level_formats_values:
            self.set_formats()

        return {
            k: v for k, v in zip(
                self.level_formats_keys, self.level_formats_values, strict=True
            )
        }

    def format(self, record):
        """
        Function that sets format linked to the level of the record
        """
        log_fmt = self.get_formats().get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    

class FileFormatter(AbstractFormatter):
    """
    File Formatter
    """

    def set_formats(self) -> None:
        """
        Method that set the self.level_formats_values
        """
        self.level_formats_values = (
            f"{self.msg_format}",
        ) * len(self.level_formats_keys)
        

class StreamFormatter(AbstractFormatter):
    """
    Stream Formatter
    """

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"


    def set_formats(self) -> None:
        """
        Method that set the self.level_formats_values
        """
        self.level_formats_values = (
            f"{self.grey}{self.msg_format}{self.reset}",
            f"{self.grey}{self.msg_format}{self.reset}",
            f"{self.yellow}{self.msg_format}{self.reset}",
            f"{self.red}{self.msg_format}{self.reset}",
            f"{self.bold_red}{self.msg_format}{self.reset}",
        )


class LoggerHandler:
    """
    Utility class that allows the user to customize the logger name with a
    single <path/filename> log file.

    Basic usage:
    - Create a logger.py file and initialize the LoggerHandler class:

      logger_handler = LoggerHandler()

    - Import the logger_handler in each file that will log messages and assign
      the result of logger_handler.get_logger(__name__) to the logger variable:

      from logger import logger_handler
      
      logger = logger_handler.get_logger(__name__)

    - Log messages with the logging.Logger methods:
      - logger.debug(<msg>)
      - logger.info(<msg>)
      - logger.warning(<msg>)
      - logger.error(<msg>)
      - logger.critical(<msg>)
    """

    def __init__(self, filename: str = "app.log", path: str = "logs") -> None:
        """
        Class initialization

        :param filename: the log filename
        :param path: the log file's path
        """
        self.filename = filename

        try:
            self.path = Path(path)
        except TypeError:
            self.path = Path("logs")
        finally:
            if not self.path.exists():
                Path.mkdir(self.path)

    def get_logger(self, logger_name: str = __name__) -> logging.Logger:
        """
        Function that initializes the logger, set the log rotation,
        configures the file_handler and stream_handler.

        :param logger_name: the logger name
        :return: a logging.Logger instance
        """

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        file_handler = TimedRotatingFileHandler(
            filename=Path.joinpath(self.path, self.filename),
            when="W6", # run each sunday
            atTime=datetime.time(23), # at 23:00
            backupCount=10 # and rotate after 10 weeks
        )
        file_handler.setFormatter(FileFormatter())
        file_handler.setLevel(logging.INFO)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(StreamFormatter())
        stream_handler.setLevel(logging.INFO)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

