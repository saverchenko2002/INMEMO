import os
import cv2

from processing.image.utils import read_grayscale
from ui.config.constants import OperationConstants

def perform_operation(source_image_path, target_image_path, str_operator):
    first_operand = read_grayscale(source_image_path)
    second_operand = read_grayscale(target_image_path)
    first_filename = os.path.splitext(os.path.basename(source_image_path))[0]
    second_filename = os.path.splitext(os.path.basename(target_image_path))[0]
    new_filename = f'{first_filename}_{str_operator}_{second_filename}.png'
    new_filename_path = os.path.join(os.path.dirname(target_image_path), new_filename)

    result_image = None

    if str_operator == OperationConstants.ADD_OPERATION.value:
        result_image = cv2.add(first_operand, second_operand)  # Сложение с обработкой переполнения
    elif str_operator == OperationConstants.SUBTRACT_OPERATION.value:
        result_image = cv2.subtract(first_operand, second_operand)

    return new_filename_path, result_image


