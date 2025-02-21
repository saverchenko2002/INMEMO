from menu.base.base_option import BaseOption

from menu.actions.preprocess_actions.smoothing_actions.gaussian_blur_action import GaussianBlurAction

class SmoothingSubmenu(BaseOption):
    def __init__(self, parent):
        super().__init__('Smoothing', parent)

        self.add_action(GaussianBlurAction(self))
