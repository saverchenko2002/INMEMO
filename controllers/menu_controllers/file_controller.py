from controllers.base_controller import BaseController

from menu.file_commands.new_project_command import NewProjectCommand
from menu.file_commands.import_image_command import ImportImageCommand

from controllers.helpers.import_image_helper import import_image
from controllers.helpers.new_project_helper import new_project


class FileController(BaseController):
    def __init__(self):
        super().__init__()

        self.add_handler(NewProjectCommand, self.handle_new_project)
        self.add_handler(ImportImageCommand, self.handle_import_image)

    def handle_new_project(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

    def handle_import_image(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

        import_image()

    def handle_new_project(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

        new_project()

