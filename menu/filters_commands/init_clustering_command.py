from core.base.command import Command
from menu.command_classes.filters_command import FiltersCommand


class InitClusteringCommand(Command, FiltersCommand):
    def __init__(self):
        super().__init__()
        print('init class InitClusteringCommand')
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
