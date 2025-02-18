import os.path

from core.base.controller import Controller
from core.app_state_service import AppStateService
from config.constants import AppStateConstants

from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.manipulate_images_command import ManipulateImagesCommand

from ui.config.constants import OperationConstants
from utils.decorators.log_comand_execution_decorator import log_command_execution
from utils.decorators.app_status_decorator import with_app_status_change


from controllers.component_controllers_helpers.manipulate_images_helper import perform_operation

from processing.image.utils import save_image

from controllers.menu_controllers_helpers.init_clustering_helper import add_images_to_tab_map

class ImageThumbnailTileComponentController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(ManipulateImagesCommand, self.handle_manipulate_images)

    @with_app_status_change
    @log_command_execution
    def handle_manipulate_images(self, command):
        first_operand = command.__dict__.get(OperationConstants.SOURCE_OPERAND.value)
        second_operand = command.__dict__.get(OperationConstants.TARGET_OPERAND.value)
        str_operator = command.__dict__.get(OperationConstants.OPERATION_OPERATOR.value)

        new_filename_path, image_data = perform_operation(first_operand, second_operand, str_operator)

        filename = save_image(new_filename_path, image_data, True)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_tab_images_map = add_images_to_tab_map(os.path.dirname(filename), [filename], tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, filename)



