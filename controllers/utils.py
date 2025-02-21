import cv2
import os
import copy

from schema.ImageModel import ImageModel


def add_images_to_tabs(image_models: [ImageModel], tab_images_map: dict[str: list[ImageModel]]):
    updated_tab_images_map = copy.deepcopy(tab_images_map)

    for image_model in image_models:
        dir_ = os.path.dirname(image_model.current_image_path)
        updated_tab_images_map.setdefault(dir_, []).append(image_model)

    return updated_tab_images_map


def save_image(image_path, image_data):
    cv2.imwrite(image_path, image_data)
    return image_path


def get_unique_filename(image_path):
    filename = os.path.basename(image_path)
    dir_ = os.path.dirname(image_path)
    name, ext = os.path.splitext(filename)

    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(dir_, new_filename)):
        new_filename = f'{name}_{counter}{ext}'
        counter += 1

    return os.path.normpath(os.path.join(dir_, new_filename))
