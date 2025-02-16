from core.base.command import Command
from menu.commands.command_classes.filters_command import FiltersCommand


class InitMorphologyCommand(Command, FiltersCommand):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('init class InitMorphologyCommand', kwargs)
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
