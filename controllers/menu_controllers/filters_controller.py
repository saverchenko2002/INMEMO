from core.app_state_service import AppStateService
from config.constants import AppStateConstants
from menu.config.constants import MenuCommandsConstants
from processing.image.constants import MorphologicalConstants

from core.base.controller import Controller

from menu.commands.filters_commands.init_clustering_command import InitClusteringCommand
from menu.commands.filters_commands.init_dilation_command import InitDilationCommand
from menu.commands.filters_commands.init_erosion_command import InitErosionCommand
from menu.commands.filters_commands.init_morphology_command import InitMorphologyCommand

from utils.decorators.app_status_decorator import with_app_status_change

from controllers.menu_controllers_helpers.init_clustering_helper import (get_clusters_number,
                                                                         create_clustering_directory,
                                                                         update_tab_images_map)

from controllers.menu_controllers_helpers.init_morphology_helper import (get_iterations_number,
                                                                         get_kernel_size,
                                                                         create_morphology_directory,
                                                                         save_filtered_image)

from controllers.menu_controllers_helpers.import_image_helper import (copy_image
                                                                      )

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

    @with_app_status_change
    def handle_init_clustering(self, command):
        print(f"Обработка команды {command.__class__.__name__}")

        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        project_directory_path = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)

        classes_num = get_clusters_number()
        clustering_directory = create_clustering_directory(project_directory_path, primary_image_path)

        clustering_image_paths = kmeans_method(primary_image_path, clustering_directory, classes_num)

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        updated_tab_images_map = update_tab_images_map(clustering_directory, clustering_image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, clustering_directory)

    @with_app_status_change
    def handle_init_erosion(self, command):
        print(f"Обработка команды {command.__class__.__name__}")

        print(f"Обработка команды {command.__class__.__name__}")
        morphology_type = MorphologicalConstants.MORPH_EROSION.name
        print(f"morphology_type в handle_init_erosion: {morphology_type}")
        image_paths = set()
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        iterations_number = get_iterations_number()
        kernel_size = get_kernel_size()
        image_data = erosion_method(primary_image_path, kernel_size, iterations_number)
        morphology_directory = create_morphology_directory(
            project_directory,
            primary_image_path,
            MorphologicalConstants.MORPH_EROSION.name
        )
        image_path = save_filtered_image(
            image_data,
            primary_image_path,
            morphology_directory,
            MorphologicalConstants.MORPH_EROSION.name
        )

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        copied_image = copy_image(primary_image_path, morphology_directory)

        image_paths.add(image_path)
        image_paths.add(copied_image)


        updated_tab_images_map = update_tab_images_map(morphology_directory, image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, morphology_directory)

        pass

    @with_app_status_change
    def handle_init_dilation(self, command):
        print(f"Обработка команды {command.__class__.__name__}")
        morphology_type = MorphologicalConstants.MORPH_EROSION.name
        print(f"morphology_type в handle_dilateion_erosion: {morphology_type}")

        image_paths = set()
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        project_directory = AppStateService().get_state(AppStateConstants.PROJECT_DIRECTORY.value)
        iterations_number = get_iterations_number()
        kernel_size = get_kernel_size()
        image_data = dilation_method(primary_image_path, kernel_size, iterations_number)
        morphology_directory = create_morphology_directory(
            project_directory,
            primary_image_path,
            MorphologicalConstants.MORPH_DILATION.name
        )
        image_path = save_filtered_image(
            image_data,
            primary_image_path,
            morphology_directory,
            MorphologicalConstants.MORPH_DILATION.name
        )

        tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)

        copied_image = copy_image(primary_image_path, morphology_directory)

        image_paths.add(image_path)
        image_paths.add(copied_image)

        updated_tab_images_map = update_tab_images_map(morphology_directory, image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, morphology_directory)


    @with_app_status_change
    def handle_init_morphology(self, command):
        print(f"Обработка команды {command.__class__.__name__} "
              f"{command.__dict__.get(MenuCommandsConstants.MORPHOLOGY_COMMAND_PAYLOAD.name)}")
        image_paths = set()
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

        image_paths.add(image_path)
        image_paths.add(copied_image)

        updated_tab_images_map = update_tab_images_map(morphology_directory, image_paths, tab_images_map)

        AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)
        AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, image_path)
        AppStateService().set_state(AppStateConstants.PRIMARY_TAB.value, morphology_directory)

        pass


