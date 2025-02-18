from menu.base.base_option import BaseOption

from menu.actions.contours_actions.find_contours_action import FindContoursAction

class ContoursOption(BaseOption):
    def __init__(self, parent):
        super().__init__("Contours", parent)

        self.add_action(FindContoursAction(self))

