from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_threshold_command import InitThresholdCommand

from menu.config.constants import MenuCommandsConstants
from processing.image.constants import ThresholdConstants


class ThresholdBinaryAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Binary', self.init_command)

    def init_command(self):
        return InitThresholdCommand(
            **{MenuCommandsConstants.THRESHOLD_COMMAND_PAYLOAD.name: ThresholdConstants.THRESH_BINARY.name}
        )


