from menu.base.base_action import BaseAction

from menu.commands.file_commands.new_project_command import NewProjectCommand

class NewProjectAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'New Project...', self.init_command)

    def init_command(self):
        return NewProjectCommand()
