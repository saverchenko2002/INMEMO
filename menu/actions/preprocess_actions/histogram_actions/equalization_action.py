from menu.base.base_action import BaseAction
from menu.commands.preprocess_commands.init_equalization_command import InitEqualizationCommand

class EqualizationAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'GHE', self.init_command)

    def init_command(self):
        return InitEqualizationCommand()