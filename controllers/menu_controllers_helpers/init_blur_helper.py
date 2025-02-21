import os

from PyQt6.QtWidgets import QInputDialog, QMessageBox

from controllers.utils import save_image, get_unique_filename
from processing.image.methods.blurs import gaussian_blur_method


def perform_gaussian_blur(image_path, kernel_size, sigma_x, sigma_y):
    image_data = gaussian_blur_method(image_path, kernel_size, sigma_x, sigma_y)
    dir_ = os.path.dirname(image_path)
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    new_filename = os.path.join(dir_, f'{name}_GBLUR{ext}')
    new_filename = get_unique_filename(new_filename)

    return save_image(new_filename, image_data)


def get_gaussian_blur_parameters(default_sigma_x=1, default_sigma_y = 1, default_kernel_size = (1,1)):
    while True:
        sigma_x, ok1 = QInputDialog.getInt(None, "Ввод параметров Gaussian Blur",
                                                "Введите значение sigmaX (число с плавающей точкой):",
                                                value=default_sigma_x, min=0)

        if not ok1:
            return None

        sigma_y, ok2 = QInputDialog.getInt(None, "Ввод параметров Gaussian Blur",
                                                "Введите значение sigmaY (число с плавающей точкой):",
                                                value=default_sigma_y, min=0)

        if not ok2:
            return None

        kernel_size_input, ok3 = QInputDialog.getText(None, "Ввод параметров Gaussian Blur",
                                                   "Введите размер kernelsize (ширина, высота), например, 8,8:",
                                                   text=f"{default_kernel_size[0]},{default_kernel_size[1]}")

        if not ok3:
            return None

        try:
            x_size, y_size = map(int, kernel_size_input.split(','))
            if x_size < 1 or y_size < 1:
                raise ValueError("Размеры kernelsize должны быть больше или равны 1.")
        except ValueError as e:
            QMessageBox.warning(None, "Ошибка ввода", f"Неверный формат данных: {e}")
            continue

        return (x_size, y_size), sigma_x, sigma_y
