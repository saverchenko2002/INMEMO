from controllers.base_controller import BaseController

from menu.file_commands.import_image_command import ImportImageCommand

from controllers.helpers.import_image_helper import import_image

class FileController(BaseController):
    def __init__(self):
        super().__init__()

        self.handlers = {
            ImportImageCommand: self.handle_import_image
        }

    def execute(self, command):
        handler = self.handlers.get(command.__class__)
        print(command.__class__)
        print(type(command))
        if handler:
            handler(command)
        else:
            print(f"Нет обработчика для команды: {command.__class__.__name__}")

    def handle_import_image(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

        import_image()
