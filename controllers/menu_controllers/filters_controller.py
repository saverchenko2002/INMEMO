from core.app_state_service import AppStateService
from config.constants import AppStateConstants

from core.base.controller import Controller

from menu.filters_commands.init_clustering_command import InitClusteringCommand

from utils.decorators.app_status_decorator import with_app_status_change

from controllers.menu_controllers_helpers.init_clustering_helper import (get_clusters_number,
                                                                         create_clustering_directory,
                                                                         update_tab_images_map)

from image_processing.methods.kmeans import kmeans_method


class FiltersController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(InitClusteringCommand, self.handle_init_clustering)

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
