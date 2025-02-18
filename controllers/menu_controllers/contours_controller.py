from PyQt6.QtWidgets import QDialog

from core.base.controller import Controller
from core.app_state_service import AppStateService

from config.constants import AppStateConstants

from menu.commands.contours_commands.find_contours_command import FindContoursCommand
from utils.decorators.app_status_decorator import with_app_status_change
from utils.decorators.log_comand_execution_decorator import log_command_execution

from ui.components.combo_enum_dialog_component.combo_enum_dialog_component import ComboEnumDialogComponent

from ui.config.constants import ContoursRetrieveOptions, ContoursChainMethods

from controllers.menu_controllers_helpers.find_contours_helper import perform_draw_contours, contours_method
from controllers.menu_controllers_helpers.init_clustering_helper import add_images_to_tab_map
import os
import logging
class ContoursController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(FindContoursCommand, self.handle_find_contours)

    @with_app_status_change
    @log_command_execution
    def handle_find_contours(self, command):
        dialog = ComboEnumDialogComponent([ContoursRetrieveOptions, ContoursChainMethods])

        if dialog.exec() == QDialog.DialogCode.Accepted:
            selections = dialog.get_selections()
            logging.info(selections)
            project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
            primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)

            new_image_filepath = perform_draw_contours(project_directory, primary_image_path, selections[0], selections[1])

            tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

            updated_tab_images_map = add_images_to_tab_map(os.path.dirname(new_image_filepath), [new_image_filepath], tab_images_map)

            AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
            AppStateService().set_state(AppStateConstants.PRIMARY_TAB.name, os.path.dirname(new_image_filepath))
            AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, new_image_filepath)

        else:
            return
