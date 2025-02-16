from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_morphology_command import InitMorphologyCommand
from menu.config.constants import MenuCommandsConstants
from processing.image.constants import MorphologicalConstants


class MorphBlackhat(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Black Hat', self.init_command)

    def init_command(self):
        return InitMorphologyCommand(
            **{MenuCommandsConstants.MORPHOLOGY_COMMAND_PAYLOAD.name: MorphologicalConstants.MORPH_BLACKHAT.name}
        )
