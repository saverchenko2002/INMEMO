from menu.base.base_option import BaseOption
from menu.actions.file_actions.new_project_action import NewProjectAction
from menu.actions.file_actions.import_image_action import ImportImageAction


class FileOption(BaseOption):
    def __init__(self, parent):
        super().__init__("File", parent)

        self.add_action(NewProjectAction(self))
        self.add_action(ImportImageAction(self))
