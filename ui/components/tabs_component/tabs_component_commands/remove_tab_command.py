from core.base.command import Command
from ui.command_classes.tabs_component_command import TabsComponentCommand


class RemoveTabCommand(Command, TabsComponentCommand):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
