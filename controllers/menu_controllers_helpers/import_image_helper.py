import copy
import os
import shutil
from pathlib import Path
from config.constants import AppStateConstants, AppStatusConstants

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
    shutil.copy(source_path, destination_path)
    return str(destination_path)


def update_tab_images_map(import_directory, image_file_path, tab_images_map):
    updated_map = copy.deepcopy(tab_images_map)
    updated_map.setdefault(import_directory, set()).add(image_file_path)

    return updated_map
