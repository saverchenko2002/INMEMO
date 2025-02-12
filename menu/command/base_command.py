from abc import ABC, abstractmethod

from core.command_publisher import CommandPublisher


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    def notify_observers(self):
        CommandPublisher.notify(self)
