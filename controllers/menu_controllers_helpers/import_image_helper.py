import copy
import os
import shutil
from pathlib import Path

from processing.image.utils import get_unique_filename

from PyQt6.QtWidgets import QFileDialog


def get_image_path():
    options = QFileDialog.Option.DontUseNativeDialog
    image_path, _ = QFileDialog.getOpenFileName(None, "Выберите изображение", "",
                                          "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)

    return image_path


def get_import_directory(project_directory):
    import_directory = os.path.join(project_directory, 'Import')
    if not os.path.exists(import_directory):
        os.makedirs(import_directory)
    return import_directory


def copy_image(source_path, destination_folder):
    source_path = Path(source_path)
    destination_folder = Path(destination_folder)
    destination_path = destination_folder / source_path.name
    destination_path = get_unique_filename(os.path.dirname(destination_path), destination_path) \
        if destination_path.exists() \
        else destination_path
    return str(shutil.copy(source_path, destination_path))


def add_image_to_tab_map(directory_path, image_file_path, tab_images_map):
    """
    Updates the tab images map by adding a new image file to the corresponding directory.

    :param directory_path: The path to the directory containing images for a tab.
    :type directory_path: str
    :param image_file_path: The path to the image file being added.
    :type image_file_path: str
    :param tab_images_map: A dictionary where each key is a directory path,
        and the value is a list of image file paths stored in that directory.
    :type tab_images_map: dict[str, list[str]]
    :return: A new copy of `tab_images_map` with the added image file.
    :rtype: dict[str, list[str]]
    """
    updated_tab_images_map = copy.deepcopy(tab_images_map)

    if directory_path not in updated_tab_images_map:
        updated_tab_images_map[directory_path] = []

    if image_file_path not in updated_tab_images_map[directory_path]:
        updated_tab_images_map[directory_path].append(image_file_path)

    return updated_tab_images_map
