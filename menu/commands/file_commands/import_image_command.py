from core.base.command import Command
from menu.commands.command_classes.file_command import FileCommand

class ImportImageCommand(Command, FileCommand):
    def __init__(self):
        super().__init__()
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
