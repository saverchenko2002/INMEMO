import shutil
import os
import copy


def get_primary_content(removable_tab_path, primary_tab_path, primary_image_path, tab_images_map):

    updated_tab_images_map = copy.deepcopy(tab_images_map)
    updated_primary_tab_path = None
    updated_primary_image_path = None

    updated_tab_images_map.pop(removable_tab_path)

    if primary_tab_path == removable_tab_path and primary_image_path in tab_images_map[removable_tab_path]:
        for tab_path, images in tab_images_map.items():
            if tab_path == removable_tab_path:
                continue
            elif images:
                updated_primary_image_path = images[0]
                updated_primary_tab_path = tab_path
                break
    elif primary_tab_path == removable_tab_path and primary_image_path not in tab_images_map[removable_tab_path]:
        for tab_path, images in tab_images_map.items():
            if primary_image_path in images:
                updated_primary_tab_path = tab_path
                updated_primary_image_path = primary_image_path
                break
    elif primary_tab_path != removable_tab_path and primary_image_path not in tab_images_map[removable_tab_path]:
        for tab_path, images in tab_images_map.items():
            if tab_path != removable_tab_path and images:
                updated_primary_image_path = images[0]
                updated_primary_tab_path = tab_path

    return updated_primary_image_path, updated_primary_tab_path, updated_tab_images_map


def remove_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
