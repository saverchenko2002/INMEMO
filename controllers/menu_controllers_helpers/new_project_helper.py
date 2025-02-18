import os.path

from PyQt6.QtWidgets import QFileDialog


def new_project():
    options = QFileDialog.Option.DontUseNativeDialog
    directory = QFileDialog.getExistingDirectory(None, "Выберите рабочую директорию", options=options)
    return os.path.normpath(directory)
