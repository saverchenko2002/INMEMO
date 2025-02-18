from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_rembg_command import InitRembgCommand


class RemoveBackgroundAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Remove Background', self.init_command)

    def init_command(self):
        return InitRembgCommand()


