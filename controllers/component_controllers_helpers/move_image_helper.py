import os.path
import copy
import shutil
from processing.image.utils import get_unique_filename

from ui.config.constants import FileSystemControlFlags

from schema.ImageModel import ImageModel

def move_image(source_image_path, target_image_path):
    target_image_path = get_unique_filename(os.path.dirname(target_image_path), target_image_path)
    shutil.move(source_image_path, target_image_path)
    return target_image_path


def move_update_tab_map(source_image_path, target_image_path, tab_images_map):
    updated_tab_images_map = copy.deepcopy(tab_images_map)
    source_dir = os.path.dirname(source_image_path)
    target_dir = os.path.dirname(target_image_path)

    index_to_remove = next(
        (i for i, img in enumerate(tab_images_map[source_dir]) if img.current_image_path == source_image_path), None)

    image_to_remove = tab_images_map[source_dir][index_to_remove]
    image_to_remove.filesystem_flag = FileSystemControlFlags.REMOVE_F

    updated_tab_images_map[source_dir] = [img for img in tab_images_map[source_dir] if img.current_image_path != source_image_path]
    updated_tab_images_map[source_dir].append(image_to_remove)

    updated_tab_images_map[target_dir].append(ImageModel(current_image_path=target_image_path, filesystem_flag=FileSystemControlFlags.ADD_F))

    # updated_tab_images_map[source_dir] = [img for img in tab_images_map[source_dir] if img.current_image_path != source_image_path]
    #
    # updated_tab_images_map[target_dir].append(ImageModel(current_image_path=target_image_path))

    return updated_tab_images_map




