from menu.command.base_command import BaseCommand
from menu.command.file_command import FileCommand


class NewProjectCommand(BaseCommand, FileCommand):
    def __init__(self):
        print('init class NewProjectCommand')
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
