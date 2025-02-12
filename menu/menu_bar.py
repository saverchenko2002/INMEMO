from PyQt6.QtWidgets import QMenuBar
from menu.options.file_option import FileOption
from menu.options.edit_option import EditOption


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.addMenu(FileOption(self))
        self.addMenu(EditOption(self))
