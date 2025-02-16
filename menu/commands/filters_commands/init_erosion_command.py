from core.base.command import Command
from menu.commands.command_classes.filters_command import FiltersCommand


class InitErosionCommand(Command, FiltersCommand):
    def __init__(self):
        super().__init__()
        print('init class InitErosionCommand')
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
