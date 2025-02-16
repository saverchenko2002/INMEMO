from PyQt6.QtWidgets import QStyle, QApplication

from menu.base.base_action import BaseAction

from menu.commands.file_commands.open_project_command import OpenProjectCommand


class OpenProjectAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Open Project...', self.init_command)
        self.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DirIcon))

    def init_command(self):
        return OpenProjectCommand()
