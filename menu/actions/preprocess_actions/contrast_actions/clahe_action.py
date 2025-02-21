from menu.base.base_action import BaseAction
from menu.commands.preprocess_commands.init_clahe_command import InitClaheCommand

class ClaheAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'CLAHE', self.init_command)

    def init_command(self):
        return InitClaheCommand()
