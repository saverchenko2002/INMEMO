from core.base.command import Command
from menu.commands.command_classes.file_command import FileCommand


class OpenProjectCommand(Command, FileCommand):
    def __init__(self):
        super().__init__()
        print('init class OpenProjectCommand')
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
