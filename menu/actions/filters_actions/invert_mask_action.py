from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_invert_mask_command import InitInvertMaskCommand
from menu.config.constants import MenuCommandsConstants


class InvertMaskAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Invert Mask', self.init_command)

    def init_command(self):
        return InitInvertMaskCommand()
