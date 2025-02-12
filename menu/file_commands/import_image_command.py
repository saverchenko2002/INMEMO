from menu.command.base_command import Command
from menu.command.file_command import FileCommand


class ImportImageCommand(Command, FileCommand):
    def __init__(self):
        print('init class ImportImageCommand')
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
