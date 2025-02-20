import os.path

from PyQt6.QtWidgets import QInputDialog, QMessageBox
import copy
from schema.ImageModel import ImageModel
def get_clusters_number():
    while True:
        num, ok = QInputDialog.getInt(None, "Ввод числа", "Введите натуральное число:", min=2)
        if not ok:
            return None
        if num > 0:
            return num
        QMessageBox.warning(None, "Ошибка ввода", "Введите натуральное число (1, 2, 3...)!")


def create_clustering_directory(project_directory, image_path):
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    clustering_directory = os.path.join(project_directory, f'{file_name}_Clustering')
    if not os.path.exists(clustering_directory):
        os.makedirs(clustering_directory)
    return os.path.normpath(clustering_directory)


def add_images_to_tab_map(directory_path, image_models: list[ImageModel], tab_images_map):
    """
    :param directory_path:
    :type directory_path: str
    :param image_models:
    :type image_models: list[ImageModel]
    :param tab_images_map:
    :type tab_images_map: dict[str, list[ImageModel]]
    :rtype: dict[str, list[str]]
    """
    updated_tab_images_map = copy.deepcopy(tab_images_map)
    updated_tab_images_map.setdefault(directory_path, []).extend(image_models)
    return updated_tab_images_map
