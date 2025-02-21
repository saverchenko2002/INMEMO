from menu.commands.command_classes.preprocess_command import PreprocessCommand
from core.base.command import Command


class InitGaussianBlurCommand(Command, PreprocessCommand):
    def __init__(self):
        super().__init__()
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()