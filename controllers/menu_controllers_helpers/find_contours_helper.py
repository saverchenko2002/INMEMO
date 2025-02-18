import os.path

from controllers.menu_controllers_helpers.import_image_helper import copy_image
from processing.image.methods.contours import contours_method, draw_contours_method
import cv2
import logging

def perform_draw_contours(project_directory, image_file_path, retrieve_option, chain_option):
    contours, hierarchy = contours_method(image_file_path, retrieve_option, chain_option)
    contours_directory = get_contours_directory(project_directory)

    copied_image_file_path = copy_image(image_file_path, contours_directory)

    output_image_path = os.path.join(contours_directory, f"contours_{os.path.basename(image_file_path)}")

    image_data = draw_contours_method(copied_image_file_path, contours, hierarchy)

    if image_data is not None:
        cv2.imwrite(output_image_path, image_data)
        return output_image_path
    else:
        logging.error("Ошибка: draw_contours_method вернул None")
        return copied_image_file_path
def get_contours_directory(project_directory):
    contours_directory = os.path.join(project_directory, 'Contours')
    if not os.path.exists(contours_directory):
        os.makedirs(contours_directory)
    return os.path.normpath(contours_directory)