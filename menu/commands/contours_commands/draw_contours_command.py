from core.base.command import Command
from menu.commands.command_classes.contours_command import ContoursCommand


class DrawContoursCommand(Command, ContoursCommand):
    def __init__(self):
        super().__init__()
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
