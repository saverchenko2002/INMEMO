from core.base.controller import Controller
from core.app_state_service import AppStateService

from config.constants import AppStateConstants

from schema.ImageModel import ImageModel
from ui.config.constants import FileSystemControlFlags

from menu.commands.preprocess_commands.init_clahe_command import InitClaheCommand
from menu.commands.preprocess_commands.init_ghe_command import InitGheCommand

from menu.commands.preprocess_commands.init_gaussian_blur_command import InitGaussianBlurCommand

from utils.decorators.app_status_decorator import with_app_status_change
from utils.decorators.reset_filesystem_flags import reset_filesystem_flags
from utils.decorators.log_comand_execution_decorator import log_command_execution

from controllers.utils import save_image, get_unique_filename, add_images_to_tabs
from controllers.menu_controllers_helpers.init_equalization_helper import get_clahe_parameters, perform_ghe, perform_clahe
from controllers.menu_controllers_helpers.init_blur_helper import get_gaussian_blur_parameters, perform_gaussian_blur

class PreprocessController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(InitGheCommand, self.handle_init_ghe)
        self.add_handler(InitClaheCommand, self.handle_init_clahe)
        self.add_handler(InitGaussianBlurCommand, self.handle_init_gaussian_blur)

    @with_app_status_change
    @reset_filesystem_flags
    @log_command_execution
    def handle_init_gaussian_blur(self, command):
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)

        result = get_gaussian_blur_parameters()

        if result is None:
            return

        kernel_size, sigma_x, sigma_y = result

        new_image_path = perform_gaussian_blur(primary_image_path, kernel_size, sigma_x, sigma_y)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_tab_images_map = add_images_to_tabs(
            [ImageModel(current_image_path=new_image_path, filesystem_flag=FileSystemControlFlags.ADD_F)],
            tab_images_map
        )

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, new_image_path)
        pass

    @with_app_status_change
    @reset_filesystem_flags
    @log_command_execution
    def handle_init_ghe(self, command):
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        new_image_path = perform_ghe(primary_image_path)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_tab_images_map = add_images_to_tabs(
            [ImageModel(current_image_path=new_image_path, filesystem_flag=FileSystemControlFlags.ADD_F)],
            tab_images_map
        )

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, new_image_path)

    @with_app_status_change
    @reset_filesystem_flags
    @log_command_execution
    def handle_init_clahe(self, command):
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        result = get_clahe_parameters()

        if result is None:
            return

        clip_limit, tile_grid_size = result

        new_image_path = perform_clahe(primary_image_path, clip_limit, tile_grid_size)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_tab_images_map = add_images_to_tabs(
            [ImageModel(current_image_path=new_image_path, filesystem_flag=FileSystemControlFlags.ADD_F)],
            tab_images_map
        )

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, new_image_path)
