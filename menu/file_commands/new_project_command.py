from core.base.command import Command
from menu.command_classes.file_command import FileCommand


class NewProjectCommand(Command, FileCommand):
    def __init__(self):
        super().__init__()
        print('init class NewProjectCommand')
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
