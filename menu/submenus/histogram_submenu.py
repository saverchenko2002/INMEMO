from menu.base.base_option import BaseOption

from menu.actions.preprocess_actions.histogram_actions.equalization_action import EqualizationAction
from menu.actions.preprocess_actions.histogram_actions.clahe_action import ClaheAction

class HistogramSubmenu(BaseOption):
    def __init__(self, parent):
        super().__init__('Histogram', parent)

        self.add_action(EqualizationAction(self))
        self.add_action(ClaheAction(self))
