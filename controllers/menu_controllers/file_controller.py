from core.app_state_service import AppStateService
from config.constants import AppStateConstants

from core.base.controller import Controller

from menu.commands.file_commands.new_project_command import NewProjectCommand
from menu.commands.file_commands.import_image_command import ImportImageCommand

from utils.decorators.app_status_decorator import with_app_status_change

from controllers.menu_controllers_helpers.import_image_helper import (get_import_directory,
                                                                      get_image_path,
                                                                      copy_image,
                                                                      update_tab_images_map)

from controllers.menu_controllers_helpers.new_project_helper import new_project


class FileController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(NewProjectCommand, self.handle_new_project)
        self.add_handler(ImportImageCommand, self.handle_import_image)

    @with_app_status_change
    def handle_import_image(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        image_file_path = get_image_path()
        import_directory = get_import_directory(project_directory)
        image_file_path = copy_image(image_file_path, import_directory)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_images_map = update_tab_images_map(import_directory, image_file_path, tab_images_map)

        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_file_path)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_images_map)

        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, import_directory)

    def handle_new_project(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

        AppStateService().set_state(AppStateConstants.PROJECT_DIRECTORY.value, new_project())
        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, {})


