from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_erosion_command import InitErosionCommand


class ErosionAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Erosion', self.init_command)

    def init_command(self):
        return InitErosionCommand()
