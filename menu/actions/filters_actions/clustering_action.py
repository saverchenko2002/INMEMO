from menu.base.base_action import BaseAction

from menu.commands.filters_commands.init_clustering_command import InitClusteringCommand


class ClusteringAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'Clustering', self.init_command)

    def init_command(self):
        return InitClusteringCommand()


