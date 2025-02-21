from PyQt6.QtWidgets import QMenuBar
from menu.options.file_option import FileOption
from menu.options.edit_option import EditOption
from menu.options.filters_option import FiltersOption
from menu.options.contours_option import ContoursOption

from menu.options.preprocess_option import PreprocessOption

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.addMenu(FileOption(self))
        self.addMenu(EditOption(self))
        self.addMenu(FiltersOption(self))
        self.addMenu(ContoursOption(self))
        self.addMenu(PreprocessOption(self))
