from abc import ABC, abstractmethod

from core.command_publisher import CommandPublisher
import logging


class Command(ABC):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        logging.info(f'init class {self.__class__.__name__}')
        pass

    @abstractmethod
    def execute(self):
        pass

    def notify_observers(self):
        CommandPublisher.notify(self)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]