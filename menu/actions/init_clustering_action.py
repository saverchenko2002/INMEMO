from menu.actions.base_action import BaseAction

from menu.filters_commands.init_clustering_command import InitClusteringCommand


class InitClusteringAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Clustering', self.init_command)

    def init_command(self):
        return InitClusteringCommand()


