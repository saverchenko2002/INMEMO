from enum import Enum



class AppStateConstants(Enum):
    PROJECT_DIRECTORY = 'project_directory'
    IMPORT_DIRECTORY = 'import_directory'

    TAB_IMAGES_MAP = 'tab_images_map'
    PRIMARY_TAB = 'primary_tab'
    PRIMARY_IMAGE_PATH = 'primary_image_path'

    APP_STATUS = 'app_status'


class AppStatusConstants(Enum):
    IDLE = 'Idle'
    BUSY = 'Busy'


class AppNameConstants(Enum):
    APPLICATION_TITLE = 'Image Processing App'
