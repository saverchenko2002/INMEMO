from menu.base.base_action import BaseAction

from menu.commands.file_commands.import_image_command import ImportImageCommand


class ImportImageAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Import Image', self.init_command)

    def init_command(self):
        return ImportImageCommand()
