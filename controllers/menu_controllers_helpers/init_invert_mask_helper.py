import copy

from processing.image.methods.masks import mask_invert_method
from schema.ImageModel import ImageModel
from ui.config.constants import FileSystemControlFlags


def perform_invert_mask(image_file_path):
    image_data = mask_invert_method(image_file_path)
    return image_file_path, image_data


def update_flag(update_image_path: str, tab_images_map: dict[str, list[ImageModel]]):
    updated_tab_images_map = copy.deepcopy(tab_images_map)

    for dir_, images in updated_tab_images_map.items():
        for image in images:
            if image.current_image_path == update_image_path:
                image.filesystem_flag = FileSystemControlFlags.UPDATE_F
                return updated_tab_images_map
