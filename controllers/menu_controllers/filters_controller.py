import logging
import os.path

from core.app_state_service import AppStateService
from config.constants import AppStateConstants
from menu.config.constants import MenuCommandsConstants
from processing.image.constants import MorphologicalConstants

from core.base.controller import Controller

from menu.commands.filters_commands.init_clustering_command import InitClusteringCommand
from menu.commands.filters_commands.init_dilation_command import InitDilationCommand
from menu.commands.filters_commands.init_erosion_command import InitErosionCommand
from menu.commands.filters_commands.init_morphology_command import InitMorphologyCommand
from menu.commands.filters_commands.init_rembg_command import InitRembgCommand

from utils.decorators.app_status_decorator import with_app_status_change
from utils.decorators.log_comand_execution_decorator import log_command_execution

from processing.image.utils import save_image

from controllers.menu_controllers_helpers.init_clustering_helper import (get_clusters_number,
                                                                         create_clustering_directory,
                                                                         add_images_to_tab_map)

from controllers.menu_controllers_helpers.init_morphology_helper import (get_iterations_number,
                                                                         get_kernel_size,
                                                                         create_morphology_directory,
                                                                         save_filtered_image)

from controllers.menu_controllers_helpers.import_image_helper import (copy_image
                                                                      )

from processing.image.methods.remove_bg import rembg_method
from processing.image.methods.kmeans import kmeans_method
from processing.image.methods.morphology import (dilation_method,
                                                 erosion_method,
                                                 morphology_method)


class FiltersController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(InitClusteringCommand, self.handle_init_clustering)
        self.add_handler(InitDilationCommand, self.handle_init_dilation)
        self.add_handler(InitErosionCommand, self.handle_init_erosion)
        self.add_handler(InitMorphologyCommand, self.handle_init_morphology)
        self.add_handler(InitRembgCommand, self.handle_init_rembg)

    @with_app_status_change
    @log_command_execution
    def handle_init_clustering(self, command):
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        project_directory_path = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)

        classes_num = get_clusters_number()
        clustering_directory = create_clustering_directory(project_directory_path, primary_image_path)

        clustering_image_paths = kmeans_method(primary_image_path, clustering_directory, classes_num)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_tab_images_map = add_images_to_tab_map(clustering_directory, clustering_image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, clustering_directory)

    @with_app_status_change
    @log_command_execution
    def handle_init_erosion(self, command):
        morphology_type = MorphologicalConstants.MORPH_EROSION.name
        image_paths = []
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        iterations_number = get_iterations_number()
        kernel_size = get_kernel_size()
        image_data = erosion_method(primary_image_path, kernel_size, iterations_number)
        morphology_directory = create_morphology_directory(
            project_directory,
            primary_image_path,
            morphology_type
        )
        image_path = save_filtered_image(
            image_data,
            primary_image_path,
            morphology_directory,
            morphology_type
        )

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        copied_image = copy_image(primary_image_path, morphology_directory)

        image_paths.append(copied_image)
        image_paths.append(image_path)

        updated_tab_images_map = add_images_to_tab_map(morphology_directory, image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, morphology_directory)


    @with_app_status_change
    @log_command_execution
    def handle_init_dilation(self, command):
        morphology_type = MorphologicalConstants.MORPH_EROSION.name

        image_paths = []
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        iterations_number = get_iterations_number()
        kernel_size = get_kernel_size()
        image_data = dilation_method(primary_image_path, kernel_size, iterations_number)
        morphology_directory = create_morphology_directory(
            project_directory,
            primary_image_path,
            morphology_type
        )
        image_path = save_filtered_image(
            image_data,
            primary_image_path,
            morphology_directory,
            morphology_type
        )

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        copied_image = copy_image(primary_image_path, morphology_directory)

        image_paths.append(copied_image)
        image_paths.append(image_path)

        updated_tab_images_map = add_images_to_tab_map(morphology_directory, image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, morphology_directory)

    @with_app_status_change
    @log_command_execution
    def handle_init_morphology(self, command):
        logging.debug(f"Обработка команды {command.__class__.__name__} "
                      f"{command.__dict__.get(MenuCommandsConstants.MORPHOLOGY_COMMAND_PAYLOAD.name)}")
        image_paths = []
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        morphology_type_str = command.__dict__.get(MenuCommandsConstants.MORPHOLOGY_COMMAND_PAYLOAD.name)
        morphology_type_enum = MorphologicalConstants[morphology_type_str].value
        kernel_size = get_kernel_size()
        image_data = morphology_method(primary_image_path, kernel_size, morphology_type_enum)

        morphology_directory = create_morphology_directory(
            project_directory,
            primary_image_path,
            morphology_type_str
        )

        image_path = save_filtered_image(
            image_data,
            primary_image_path,
            morphology_directory,
            morphology_type_str
        )

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        copied_image = copy_image(primary_image_path, morphology_directory)

        image_paths.append(copied_image)
        image_paths.append(image_path)

        updated_tab_images_map = add_images_to_tab_map(morphology_directory, image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, morphology_directory)

    @with_app_status_change
    def handle_init_rembg(self, command):

        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        image_data = rembg_method(primary_image_path)
        filename = f'{os.path.splitext(os.path.basename(primary_image_path))[0]}_rembg_.png'
        directory = os.path.dirname(primary_image_path)
        image_path = os.path.join(directory, filename)
        filename = save_image(image_path, image_data, True)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP)

        updated_tab_images_map = add_images_to_tab_map(directory,[filename], tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, filename)