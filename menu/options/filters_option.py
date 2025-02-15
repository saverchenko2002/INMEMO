from menu.options.base_option import BaseOption

from menu.actions.init_clustering_action import InitClusteringAction


class FiltersOption(BaseOption):
    def __init__(self, parent):
        super().__init__("Filters", parent)

        self.add_action(InitClusteringAction(self))

