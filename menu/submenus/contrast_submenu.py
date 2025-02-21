from menu.base.base_option import BaseOption

from menu.actions.preprocess_actions.contrast_actions.ghe_action import GheAction
from menu.actions.preprocess_actions.contrast_actions.clahe_action import ClaheAction

class ContrastSubmenu(BaseOption):
    def __init__(self, parent):
        super().__init__('Contrast', parent)

        self.add_action(GheAction(self))
        self.add_action(ClaheAction(self))
