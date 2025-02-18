from menu.base.base_option import BaseOption

from menu.submenus.morphology_submenu import MorphologySubmenu
from menu.submenus.threshold_submenu import ThresholdSubmenu
from menu.submenus.interpolation_submenu import InterpolationSubmenu

from menu.actions.filters_actions.invert_mask_action import InvertMaskAction
from menu.actions.filters_actions.clustering_action import ClusteringAction
from menu.actions.filters_actions.remove_background_action import RemoveBackgroundAction


class FiltersOption(BaseOption):
    def __init__(self, parent):
        super().__init__("Filters", parent)

        self.addMenu(ThresholdSubmenu(self))
        self.addAction(InvertMaskAction(self))
        self.addMenu(InterpolationSubmenu(self))
        self.add_action(RemoveBackgroundAction(self))
        self.add_action(ClusteringAction(self))
        self.addMenu(MorphologySubmenu(self))

