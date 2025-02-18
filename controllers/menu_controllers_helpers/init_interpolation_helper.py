import os.path

from processing.image.constants import InterpolationConstants
from processing.image.methods.interpolation import interpolation_method
from PyQt6.QtWidgets import QInputDialog, QMessageBox


def perform_interpolation(image_path, size, threshold_type):
    threshold_type_cv2 = InterpolationConstants[threshold_type].value

    image_data = interpolation_method(image_path, size, threshold_type_cv2)
    file_name = f'{os.path.splitext(os.path.basename(image_path))[0]}_{threshold_type}.png'
    file_path = os.path.join(os.path.dirname(image_path), file_name)
    return file_path, image_data


def get_image_size():
    default_width = 576
    default_height = 576
    while True:
        size_input, ok = QInputDialog.getText(None, "Размер изображения",
                                              "Введите размер (ширина, высота), например, 576,576:",
                                              text=f"{default_width},{default_height}")

        try:
            width, height = map(int, size_input.split(','))
            if width < 1 or height < 1:
                raise ValueError("Размеры изображения должны быть больше или равны 1.")
            return width, height
        except ValueError as e:
            QMessageBox.warning(None, "Ошибка ввода", f"Неверный формат данных: {e}")
            continue