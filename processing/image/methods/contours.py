import cv2
from processing.image.utils import read_grayscale
import logging

def contours_method(image_file_path, retrieve_option, chain_option):
    image_data = read_grayscale(image_file_path)
    contours, hierarchy = cv2.findContours(image_data, retrieve_option, chain_option)
    logging.info(contours)
    return contours, hierarchy


def draw_contours_method(image_file_path, contours, hierarchy, color=(0, 255, 0), thickness=2):
    image_data = read_grayscale(image_file_path)

    if image_data is None:
        logging.error(f"Ошибка загрузки изображения: {image_file_path}")
        return None

    image_data = cv2.cvtColor(image_data, cv2.COLOR_GRAY2BGR)

    if contours:
        cv2.drawContours(image_data, contours, -1, color, thickness, hierarchy=hierarchy)
    else:
        logging.warning(f"Контуры не найдены в {image_file_path}")

    return image_data
