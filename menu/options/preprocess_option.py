from menu.base.base_option import BaseOption

from menu.submenus.contrast_submenu import ContrastSubmenu
from menu.submenus.smoothing_submenu import SmoothingSubmenu


class PreprocessOption(BaseOption):
    def __init__(self, parent):
        super().__init__('Preprocess', parent)

        self.addMenu(ContrastSubmenu(self))
        self.addMenu(SmoothingSubmenu(self))
