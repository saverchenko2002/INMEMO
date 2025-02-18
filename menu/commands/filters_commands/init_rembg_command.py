from core.base.command import Command
from menu.commands.command_classes.filters_command import FiltersCommand


class InitRembgCommand(Command, FiltersCommand):
    def __init__(self):
        super().__init__()
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
