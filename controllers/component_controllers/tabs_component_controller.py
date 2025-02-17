import os.path

from core.base.controller import Controller
from core.app_state_service import AppStateService

from utils.decorators.app_status_decorator import with_app_status_change

from config.constants import AppStateConstants

from ui.components.tabs_component.tabs_component_commands.change_primary_image_command import ChangePrimaryImageCommand
from ui.components.tabs_component.tabs_component_commands.move_image_command import MoveImageCommand

from ui.config.constants import MoveToTabConstants

from controllers.component_controllers_helpers.move_image_helper import move_image, move_update_tab_map

class TabsComponentController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(ChangePrimaryImageCommand, self.handle_change_primary_image)
        self.add_handler(MoveImageCommand, self.handle_move_image)

    def handle_change_primary_image(self, command):
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        input_primary_image_path = command.__dict__.get(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        if primary_image_path != input_primary_image_path:
            AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, input_primary_image_path)

    @with_app_status_change
    def handle_move_image(self, command):
        source_image_path = command.__dict__.get(MoveToTabConstants.SOURCE_IMAGE_PATH.value)
        target_folder_name = command.__dict__.get(MoveToTabConstants.TARGET_FOLDER_NAME.value)

        project_dir = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        target_folder_path = os.path.join(project_dir, target_folder_name)
        target_image_path = os.path.join(target_folder_path, os.path.basename(source_image_path))
        print('handle_move_image', target_image_path)
        target_image_path = move_image(source_image_path, target_image_path)
        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)
        updated_tab_images_map = move_update_tab_map(source_image_path, target_image_path, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, os.path.dirname(target_image_path))
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, target_image_path)
