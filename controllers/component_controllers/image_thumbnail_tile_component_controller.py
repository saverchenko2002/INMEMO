import os.path

from core.base.controller import Controller
from core.app_state_service import AppStateService
from config.constants import AppStateConstants

from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.manipulate_images_command import ManipulateImagesCommand
from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.rename_image_command import RenameImageCommand
from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.remove_image_command import RemoveImageCommand

from ui.config.constants import OperationConstants
from ui.config.constants import ImageModelConstants
from utils.decorators.log_comand_execution_decorator import log_command_execution
from utils.decorators.app_status_decorator import with_app_status_change
from utils.decorators.reset_filesystem_flags import reset_filesystem_flags


from controllers.component_controllers_helpers.manipulate_images_helper import perform_operation

from processing.image.utils import save_image

from controllers.menu_controllers_helpers.init_clustering_helper import add_images_to_tab_map

from controllers.component_controllers_helpers.rename_image_helper import rename_image, update_tab_images_map_for_rename
from ui.config.constants import FileSystemControlFlags
from schema.ImageModel import ImageModel

from controllers.component_controllers_helpers.remove_image_helper import remove_image, update_tab_images_map_for_remove, find_new_primary_image
import logging

class ImageThumbnailTileComponentController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(ManipulateImagesCommand, self.handle_manipulate_images)
        self.add_handler(RenameImageCommand, self.handle_rename_image)
        self.add_handler(RemoveImageCommand, self.handle_remove_image)

    @with_app_status_change
    @reset_filesystem_flags
    @log_command_execution
    def handle_remove_image(self, command):
        image = command.__dict__.get(ImageModelConstants.IMAGE_MODEL.value)
        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        primary_tab = AppStateService().get_state(AppStateConstants.PRIMARY_TAB.value)

        remove_image(image)
        updated_tab_images_map = update_tab_images_map_for_remove(image, tab_images_map)
        if primary_image_path == image.current_image_path:
            primary_image_path = find_new_primary_image(image, primary_tab, updated_tab_images_map)
            AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, primary_image_path)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)


    @with_app_status_change
    @reset_filesystem_flags
    @log_command_execution
    def handle_rename_image(self, command):
        image = command.__dict__.get(ImageModelConstants.IMAGE_MODEL.value)
        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        rename_image(image, unique_filename=True)
        updated_tab_images_map = update_tab_images_map_for_rename(image, tab_images_map)

        source_image_path = image.original_image_path
        target_image_path = image.current_image_path
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)

        if source_image_path == primary_image_path:
            AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, target_image_path)




    @with_app_status_change
    @reset_filesystem_flags
    @log_command_execution
    def handle_manipulate_images(self, command):
        first_operand = command.__dict__.get(OperationConstants.SOURCE_OPERAND.value)
        second_operand = command.__dict__.get(OperationConstants.TARGET_OPERAND.value)
        str_operator = command.__dict__.get(OperationConstants.OPERATION_OPERATOR.value)

        new_filename_path, image_data = perform_operation(first_operand, second_operand, str_operator)

        filename = save_image(new_filename_path, image_data, True)

        image_model = ImageModel(current_image_path=filename, filesystem_flag=FileSystemControlFlags.ADD_F)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_tab_images_map = add_images_to_tab_map(os.path.dirname(filename), [image_model], tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, filename)



