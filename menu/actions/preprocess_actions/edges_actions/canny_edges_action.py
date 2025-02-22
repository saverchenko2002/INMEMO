from menu.base.base_action import BaseAction
from menu.commands.preprocess_commands.init_canny_edges_command import InitCannyEdgesCommand


class CannyEdgesAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Canny', self.init_command)

    def init_command(self):
        return InitCannyEdgesCommand()
