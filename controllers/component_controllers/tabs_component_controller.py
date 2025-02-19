import os.path

from core.base.controller import Controller
from core.app_state_service import AppStateService

from utils.decorators.app_status_decorator import with_app_status_change
from utils.decorators.log_comand_execution_decorator import log_command_execution

from config.constants import AppStateConstants

from ui.components.tabs_component.tabs_component_commands.change_primary_image_command import ChangePrimaryImageCommand
from ui.components.tabs_component.tabs_component_commands.move_image_command import MoveImageCommand
from ui.components.tabs_component.tabs_component_commands.remove_tab_command import RemoveTabCommand
from ui.components.tabs_component.tabs_component_commands.change_tab_command import ChangeTabCommand

from ui.config.constants import MoveToTabConstants, RemoveTabConstants, ChangeTabConstants

from controllers.component_controllers_helpers.move_image_helper import move_image, move_update_tab_map
from controllers.component_controllers_helpers.remove_tab_helper import get_primary_content, remove_directory


class TabsComponentController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(ChangePrimaryImageCommand, self.handle_change_primary_image)
        self.add_handler(MoveImageCommand, self.handle_move_image)
        self.add_handler(RemoveTabCommand, self.handle_remove_tab)
        self.add_handler(ChangeTabCommand, self.handle_change_tab)

    @with_app_status_change
    @log_command_execution
    def handle_change_tab(self, command):
        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        tab_name = command.__dict__.get(ChangeTabConstants.CHANGE_TAB_NAME.value)
        dir_path = os.path.join(project_directory, tab_name)

        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, dir_path)

    @with_app_status_change
    @log_command_execution
    def handle_remove_tab(self, command):
        dir_name = command.__dict__.get(RemoveTabConstants.REMOVE_TAB_NAME.value)

        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)

        primary_tab_path = AppStateService().get_state(AppStateConstants.PRIMARY_TAB.value)
        removable_tab_path = os.path.join(project_directory, dir_name)
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_primary_image_path, updated_primary_tab_path, updated_tab_images_map \
            = get_primary_content(removable_tab_path, primary_tab_path, primary_image_path, tab_images_map)
        remove_directory(removable_tab_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, updated_primary_image_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, updated_primary_tab_path)
        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)

    @log_command_execution
    def handle_change_primary_image(self, command):
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        input_primary_image_path = command.__dict__.get(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        if primary_image_path != input_primary_image_path:
            AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, input_primary_image_path)

    @with_app_status_change
    @log_command_execution
    def handle_move_image(self, command):
        source_image_path = command.__dict__.get(MoveToTabConstants.SOURCE_IMAGE_PATH.value)
        target_folder_name = command.__dict__.get(MoveToTabConstants.TARGET_FOLDER_NAME.value)

        project_dir = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        target_folder_path = os.path.join(project_dir, target_folder_name)
        target_image_path = os.path.join(target_folder_path, os.path.basename(source_image_path))
        target_image_path = move_image(source_image_path, target_image_path)
        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)
        updated_tab_images_map = move_update_tab_map(source_image_path, target_image_path, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, os.path.dirname(target_image_path))
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, target_image_path)
