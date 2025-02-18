from menu.base.base_action import BaseAction

from menu.commands.contours_commands.find_contours_command import FindContoursCommand


class FindContoursAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Find Contours', self.init_command)

    def init_command(self):
        return FindContoursCommand()
