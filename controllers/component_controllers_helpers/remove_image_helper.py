import copy
import os
import shutil
from schema.ImageModel import ImageModel
from processing.image.utils import get_unique_filename
from ui.config.constants import FileSystemControlFlags

def remove_image(image:ImageModel):
    image_file_path = image.current_image_path
    if os.path.exists(image_file_path):
        try:
            os.remove(image_file_path)  # Удаляем файл
        except Exception as e:
            print(f"Ошибка при удалении файла: {e}")
    else:
        print(f"Файл {image_file_path} не существует.")


def update_tab_images_map_for_remove(image_to_remove: ImageModel, tab_images_map: dict[str, list[ImageModel]]):
    updated_tab_images_map = copy.deepcopy(tab_images_map)

    for images in updated_tab_images_map.values():
        for existing_image in images:
            if existing_image.current_image_path == image_to_remove.current_image_path:
                existing_image.filesystem_flag = FileSystemControlFlags.REMOVE_F
                return updated_tab_images_map

def find_new_primary_image(image_to_remove:ImageModel, primary_image_path, primary_tab, tab_images_map: dict[str, list[ImageModel]]):

    images = tab_images_map[primary_tab]
    preserved_images = [image for image in images if image.current_image_path != image_to_remove.current_image_path]

    return preserved_images[0].current_image_path if preserved_images else None


