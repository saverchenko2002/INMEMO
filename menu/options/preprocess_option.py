from menu.base.base_option import BaseOption

from menu.submenus.histogram_submenu import HistogramSubmenu

class PreprocessOption(BaseOption):
    def __init__(self, parent):
        super().__init__('Preprocess', parent)

        self.addMenu(HistogramSubmenu(self))
