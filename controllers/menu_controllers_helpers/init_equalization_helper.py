import os

from PyQt6.QtWidgets import QInputDialog, QMessageBox

from processing.image.methods.histograms import ghe_method, clahe_method

from controllers.utils import save_image, get_unique_filename


def perform_ghe(image_path):
    image_data = ghe_method(image_path)
    dir_ = os.path.dirname(image_path)
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    new_filename = os.path.join(dir_, f'{name}_GHE{ext}')
    new_filename = get_unique_filename(new_filename)

    return save_image(new_filename, image_data)


def perform_clahe(image_path, clip_limit, tile_grid_size):
    image_data = clahe_method(image_path, clip_limit, tile_grid_size)
    dir_ = os.path.dirname(image_path)
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    new_filename = os.path.join(dir_, f'{name}_CLAHE{ext}')
    new_filename = get_unique_filename(new_filename)

    return save_image(new_filename, image_data)


def get_clahe_parameters(default_cliplimit=2.0, default_tilegridsize=(8, 8)):
    while True:
        cliplimit, ok1 = QInputDialog.getDouble(None, "Ввод параметров CLAHE",
                                                "Введите значение cliplimit (число с плавающей точкой):",
                                                value=default_cliplimit, min=0.0)

        if not ok1:
            return None

        tilegrid_input, ok2 = QInputDialog.getText(None, "Ввод параметров CLAHE",
                                                   "Введите размер tilegridsize (ширина, высота), например, 8,8:",
                                                   text=f"{default_tilegridsize[0]},{default_tilegridsize[1]}")

        if not ok2:
            return None

        try:
            tilegrid_x, tilegrid_y = map(int, tilegrid_input.split(','))
            if tilegrid_x < 1 or tilegrid_y < 1:
                raise ValueError("Размеры tilegridsize должны быть больше или равны 1.")
        except ValueError as e:
            QMessageBox.warning(None, "Ошибка ввода", f"Неверный формат данных: {e}")
            continue

        return cliplimit, (tilegrid_x, tilegrid_y)

