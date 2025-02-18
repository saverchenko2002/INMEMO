from menu.base.base_action import BaseAction

from menu.commands.contours_commands.draw_contours_command import DrawContoursCommand


class DrawContoursAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Draw Contours(BETA)', self.init_command)

    def init_command(self):
        return DrawContoursCommand()
