from menu.base.base_action import BaseAction
from menu.commands.preprocess_commands.init_gaussian_blur_command import InitGaussianBlurCommand


class GaussianBlurAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Gaussian Blur', self.init_command)

    def init_command(self):
        return InitGaussianBlurCommand()
