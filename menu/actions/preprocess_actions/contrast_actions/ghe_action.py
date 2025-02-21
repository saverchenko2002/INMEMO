from menu.base.base_action import BaseAction
from menu.commands.preprocess_commands.init_ghe_command import InitGheCommand

class GheAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'GHE', self.init_command)

    def init_command(self):
        return InitGheCommand()