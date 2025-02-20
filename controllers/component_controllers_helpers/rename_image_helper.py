import copy
import os
import shutil
from schema.ImageModel import ImageModel
from processing.image.utils import get_unique_filename
from ui.config.constants import FileSystemControlFlags

def rename_image(image: ImageModel, unique_filename=False):
    filename = image.current_image_path
    if unique_filename:
        filename = get_unique_filename(os.path.dirname(image.current_image_path), image.current_image_path)
        image.current_image_path = filename

    if not os.path.exists(image.original_image_path):
        raise FileNotFoundError(f"The file {image.original_image_path} does not exist.")

    try:
        shutil.move(image.original_image_path, filename)
    except Exception as e:
        raise Exception(f"Error moving file: {e}")

    return filename


def update_tab_images_map_for_rename(renamed_image: ImageModel, tab_images_map: dict[str, list[ImageModel]]):
    updated_tab_images_map = copy.deepcopy(tab_images_map)

    for images in updated_tab_images_map.values():
        for existing_image in images:
            if existing_image.original_image_path == renamed_image.original_image_path:
                existing_image.current_image_path = renamed_image.current_image_path
                existing_image.original_image_path = renamed_image.original_image_path
                existing_image.filesystem_flag = FileSystemControlFlags.RENAME_F
                return updated_tab_images_map

    # for images in updated_tab_images_map.values():
    #     for pre_update_image in images:
    #         if pre_update_image.original_image_path == image.original_image_path:
    #             pre_update_image.current_image_path = image.current_image_path
    #             pre_update_image.original_image_path = pre_update_image.current_image_path
    #             return updated_tab_images_map
