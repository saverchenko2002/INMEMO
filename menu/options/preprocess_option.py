from menu.base.base_option import BaseOption

from menu.submenus.contrast_submenu import ContrastSubmenu
from menu.submenus.smoothing_submenu import SmoothingSubmenu
from menu.submenus.edges_submenu import EdgesSubmenu


class PreprocessOption(BaseOption):
    def __init__(self, parent):
        super().__init__('Preprocess', parent)

        self.addMenu(ContrastSubmenu(self))
        self.addMenu(SmoothingSubmenu(self))
        self.addMenu(EdgesSubmenu(self))
