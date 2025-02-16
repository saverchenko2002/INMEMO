from PyQt6.QtWidgets import QInputDialog, QMessageBox
from processing.image.utils import save_image, get_unique_filename
import os


def save_filtered_image(image_data, primary_image_path, image_directory, morphology_type):
    print(morphology_type, "save_filtered_imagemorphology_type")
    file_name = f'{os.path.splitext(os.path.basename(primary_image_path))[0]}_{morphology_type}.png'
    file_path = os.path.join(image_directory, file_name)
    return save_image(file_path, image_data, unique_filename=True)


def create_morphology_directory(project_directory, image_file_path, morphology_type):
    print(morphology_type, "create_morphology_directorymorphology_type")
    file_name = os.path.basename(image_file_path)
    morphology_directory = (
        os.path.join(project_directory, f'{os.path.splitext(os.path.basename(file_name))[0]}_{morphology_type}'))
    if not os.path.exists(morphology_directory):
        os.makedirs(morphology_directory)
    return morphology_directory


def get_iterations_number():
    while True:
        num, ok = QInputDialog.getInt(None, "Ввод числа", "Введите натуральное число:", min=1)

        if num >= 1:
            return num

        QMessageBox.warning(None, "Ошибка ввода", "Введите натуральное число (1, 2, 3...)!")


def get_kernel_size():
    while True:
        kernel_input, ok = QInputDialog.getText(None, "Размерность ядра",
                                            "Введите размер ядра (например, 5,5):")

        try:
            x, y = map(int, kernel_input.split(','))
            if x < 1 or y < 1:
                raise ValueError("Размер ядра должен быть больше или равен 1.")
            return x, y
        except ValueError as e:
            QMessageBox.warning(None, "Ошибка ввода", f"Неверный формат данных: {e}")
            continue
