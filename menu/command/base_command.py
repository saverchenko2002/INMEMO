from abc import ABC, abstractmethod

from core.command_publisher import CommandPublisher


class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    def notify_observers(self):
        CommandPublisher.notify(self)
