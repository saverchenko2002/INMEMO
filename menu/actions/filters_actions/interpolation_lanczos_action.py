from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_interpolation_command import InitInterpolationCommand
from menu.config.constants import MenuCommandsConstants
from processing.image.constants import InterpolationConstants


class InterpolationLanczosAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Lanczos', self.init_command)

    def init_command(self):
        return InitInterpolationCommand(
            **{MenuCommandsConstants.INTERPOLATION_COMMAND_PAYLOAD.name: InterpolationConstants.INTER_LANCZOS.name}
        )
