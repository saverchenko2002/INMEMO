from core.app_state_service import AppStateService
from ui.config.constants import FileSystemControlFlags
from config.constants import AppStateConstants
from functools import wraps
import copy


def reset_filesystem_flags(func):
    @wraps(func)
    def wrapper(self, command, *args, **kwargs):

        try:
            return func(self, command, *args, **kwargs)
        finally:
            reset_flags(self)

    return wrapper


def reset_flags(self):
    tab_images_map = AppStateService().get_state(AppStateConstants.TAB_IMAGES_MAP.value)
    updated_tab_images_map = {}
    for dir_, images in tab_images_map.items():
        updated_tab_images_map[dir_] = []
        for image in images:
            if image.filesystem_flag == FileSystemControlFlags.ADD_F:
                image.filesystem_flag = FileSystemControlFlags.NONE_F
                updated_tab_images_map[dir_].append(image)
            elif image.filesystem_flag == FileSystemControlFlags.RENAME_F:
                image.original_image_path = image.current_image_path
                image.filesystem_flag = FileSystemControlFlags.NONE_F
                updated_tab_images_map[dir_].append(image)
            elif image.filesystem_flag == FileSystemControlFlags.UPDATE_F:
                image.filesystem_flag = FileSystemControlFlags.NONE_F
                updated_tab_images_map[dir_].append(image)
            elif image.filesystem_flag == FileSystemControlFlags.NONE_F:
                updated_tab_images_map[dir_].append(image)
            if not images:
                del updated_tab_images_map[dir_]
    AppStateService().set_state(AppStateConstants.TAB_IMAGES_MAP.value, updated_tab_images_map)