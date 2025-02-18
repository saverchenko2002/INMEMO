from menu.base.base_option import BaseOption

from menu.actions.filters_actions.threshold_binary_action import ThresholdBinaryAction

class ThresholdSubmenu(BaseOption):
    def __init__(self, parent):
        super().__init__('Threshold', parent)

        self.add_action(ThresholdBinaryAction(self))
