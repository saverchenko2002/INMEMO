from menu.base.base_option import BaseOption

from menu.actions.filters_actions.erosion_action import ErosionAction
from menu.actions.filters_actions.dilation_action import DilationAction
from menu.actions.filters_actions.morph_opening_action import MorphOpeningAction
from menu.actions.filters_actions.morph_closing_action import MorphClosingAction
from menu.actions.filters_actions.morph_gradient_action import MorphGradientAction
from menu.actions.filters_actions.morph_tophat_action import MorphTophatAction
from menu.actions.filters_actions.morph_blackhat_action import MorphBlackhat

class MorphologySubmenu(BaseOption):
    def __init__(self, parent):
        super().__init__('Morphology', parent)

        self.add_action(ErosionAction(self))
        self.add_action(DilationAction(self))
        self.add_action(MorphOpeningAction(self))
        self.add_action(MorphClosingAction(self))
        self.add_action(MorphGradientAction(self))
        self.add_action(MorphTophatAction(self))
        self.add_action(MorphBlackhat(self))
