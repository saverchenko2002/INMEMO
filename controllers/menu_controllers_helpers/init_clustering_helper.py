import os.path

from PyQt6.QtWidgets import QInputDialog, QMessageBox
import copy

def get_clusters_number():
    while True:
        num, ok = QInputDialog.getInt(None, "Ввод числа", "Введите натуральное число:", min=2)
        if not ok:
            return None  # Если нажата "Отмена"
        if num > 0:
            return num
        QMessageBox.warning(None, "Ошибка ввода", "Введите натуральное число (1, 2, 3...)!")


def create_clustering_directory(project_directory, image_path):
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    clustering_directory = os.path.join(project_directory, f'{file_name}_Clustering')
    if not os.path.exists(clustering_directory):
        os.makedirs(clustering_directory)
    return clustering_directory


def update_tab_images_map(import_directory, image_file_paths, tab_images_map):
    updated_map = copy.deepcopy(tab_images_map)

    updated_map.setdefault(import_directory, set()).update(image_file_paths)

    return updated_map
