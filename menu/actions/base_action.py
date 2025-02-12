from PyQt6.QtGui import QAction
from typing import Callable
from abc import abstractmethod

from menu.command.base_command import BaseCommand


class BaseAction(QAction):
    def __init__(self, parent, name: str, callback: Callable):
        super().__init__(name, parent)
        self.triggered.connect(callback)
        self.setEnabled = True

    @abstractmethod
    def init_command(self):
        return BaseCommand()
