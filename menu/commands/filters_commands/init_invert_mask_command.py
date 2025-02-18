from core.base.command import Command
from menu.commands.command_classes.filters_command import FiltersCommand


class InitInvertMaskCommand(Command, FiltersCommand):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
