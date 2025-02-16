from core.base.command import Command
from menu.commands.command_classes.filters_command import FiltersCommand


class InitDilationCommand(Command, FiltersCommand):
    def __init__(self):
        super().__init__()
        print('init class InitDilationCommand')
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
