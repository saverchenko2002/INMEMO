import os
from config.constants import AppStateConstants, AppStatusConstants

from PyQt6.QtWidgets import QFileDialog


def pick_up_image():
    options = QFileDialog.Option.DontUseNativeDialog
    file, _ = QFileDialog.getOpenFileName(None, "Выберите изображение", "",
                                          "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)

    return file


def get_import_directory(project_directory):
    import_directory = os.path.join(project_directory, 'Import')
    if not os.path.exists(import_directory):
        os.makedirs(import_directory)
    return import_directory
