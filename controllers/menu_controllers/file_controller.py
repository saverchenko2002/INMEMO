import os

from core.app_state_service import AppStateService
from config.constants import AppStateConstants

from core.base.controller import Controller

from menu.commands.file_commands.new_project_command import NewProjectCommand
from menu.commands.file_commands.import_image_command import ImportImageCommand
from menu.commands.file_commands.open_project_command import OpenProjectCommand

from utils.decorators.app_status_decorator import with_app_status_change

from controllers.menu_controllers_helpers.import_image_helper import (get_import_directory,
                                                                      get_image_path,
                                                                      copy_image,
                                                                      add_image_to_tab_map)


from controllers.menu_controllers_helpers.new_project_helper import new_project


class FileController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(NewProjectCommand, self.handle_new_project)
        self.add_handler(OpenProjectCommand, self.handle_open_project)
        self.add_handler(ImportImageCommand, self.handle_import_image)

    @with_app_status_change
    def handle_import_image(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        image_file_path = get_image_path()
        import_directory = get_import_directory(project_directory)
        image_file_path = copy_image(image_file_path, import_directory)
        print('ТО ЧТО МНЕ ИМПОРТИРУЮТ НАХУЙ', image_file_path)
        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_images_map = add_image_to_tab_map(import_directory, image_file_path, tab_images_map)

        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_file_path)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_images_map)

        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, import_directory)

    def handle_new_project(self, command):

        print(f"Обработка команды {command.__class__.__name__}")

        AppStateService().set_state(AppStateConstants.PROJECT_DIRECTORY.value, new_project())
        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, {})

    @with_app_status_change
    def handle_open_project(self, command):
        print(f"Обработка команды {command.__class__.__name__}")
        project_directory = new_project()

        subdirs = [
            os.path.join(project_directory, d)
            for d in os.listdir(project_directory)
            if os.path.isdir(os.path.join(project_directory, d))
        ]

        subdirs.sort(key=os.path.getctime)

        tab_images_map = {}

        for dir_ in subdirs:
            images = [
                os.path.join(dir_, file)
                for file in os.listdir(dir_)
                if file.lower().endswith(('.png', '.jpg', '.jpeg'))
            ]
            tab_images_map[dir_] = images

        if not tab_images_map:
            print("Ошибка: В проекте нет изображений")
            return

        primary_tab, primary_image = next(
            ((dir_, images[0]) for dir_, images in tab_images_map.items() if images),
            (None, None)
        )

        print(primary_tab, 'ПРИМЕР КАРТИНКИ НА ИМПОРТЕ С ИНИТ ПРОЕКТА')

        AppStateService().set_state(AppStateConstants.PROJECT_DIRECTORY.value, project_directory)
        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, {})
        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, primary_tab)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, primary_image)


