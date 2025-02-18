from menu.base.base_option import BaseOption

from menu.actions.filters_actions.interpolation_cubic_action import InterpolationCubicAction
from menu.actions.filters_actions.interpolation_lanczos_action import InterpolationLanczosAction
from menu.actions.filters_actions.interpolation_linear_action import InterpolationLinearAction
from menu.actions.filters_actions.interpolation_nearest_action import InterpolationNearestAction


class InterpolationSubmenu(BaseOption):
    def __init__(self, parent):
        super().__init__('Interpolation', parent)

        self.add_action(InterpolationNearestAction(self))
        self.add_action(InterpolationLinearAction(self))
        self.add_action(InterpolationCubicAction(self))
        self.add_action(InterpolationLanczosAction(self))

