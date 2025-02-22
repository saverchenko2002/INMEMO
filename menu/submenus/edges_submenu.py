from menu.base.base_option import BaseOption

from menu.actions.preprocess_actions.edges_actions.canny_edges_action import CannyEdgesAction

class EdgesSubmenu(BaseOption):
    def __init__(self, parent):
        super().__init__('Canny', parent)

        self.add_action(CannyEdgesAction(self))
