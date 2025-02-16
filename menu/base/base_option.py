from PyQt6.QtWidgets import QMenu
from menu.base.base_action import BaseAction


class BaseOption(QMenu):
    def __init__(self, title: str, parent):
        super().__init__(title, parent)

    def add_action(self, action: BaseAction):
        self.addAction(action)

