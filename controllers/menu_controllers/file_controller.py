from core.app_state_service import AppStateService
from config.constants import AppStateConstants, AppStatusConstants


from controllers.base_controller import BaseController

from menu.file_commands.new_project_command import NewProjectCommand
from menu.file_commands.import_image_command import ImportImageCommand

from controllers.helpers.import_image_helper import get_import_directory, pick_up_image
from controllers.helpers.new_project_helper import new_project


class FileController(BaseController):
    def __init__(self):
        super().__init__()

        self.add_handler(NewProjectCommand, self.handle_new_project)
        self.add_handler(ImportImageCommand, self.handle_import_image)

    def handle_import_image(self, command):

        print(f"Обработка команды {command.__class__.__name__}")
        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        image_file_path = pick_up_image()
        print('image_file_name' + image_file_path)
        #load
        AppStateService().set_state(AppStateConstants.APP_STATUS.value, AppStatusConstants.BUSY.value)
        import_directory = get_import_directory(project_directory)
        #stopload
        tab_directories_set = AppStateService().get_state(AppStateConstants.TAB_DIRECTORIES.value)
        tab_directories_set.add(import_directory)
        AppStateService().set_state(AppStateConstants.TAB_DIRECTORIES.value, tab_directories_set)

        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_file_path)

        print(AppStateConstants.PROJECT_DIRECTORY.value)
        print(AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value))

        AppStateService().set_state(AppStateConstants.APP_STATUS.value, AppStatusConstants.IDLE.value)


    def handle_new_project(self, command):

        print(f"Обработка команды {command.__class__.__name__}")
        print('FileController сначала я получаю доступ')

        AppStateService().set_state(AppStateConstants.PROJECT_DIRECTORY.value, new_project())
        AppStateService().set_state(AppStateConstants.TAB_DIRECTORIES.value, set())

        print('FileController сначала я получаю доступ')

