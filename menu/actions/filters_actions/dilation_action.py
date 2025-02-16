from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_dilation_command import InitDilationCommand


class DilationAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Dilation', self.init_command)

    def init_command(self):
        return InitDilationCommand()
