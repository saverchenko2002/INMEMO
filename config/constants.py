from enum import Enum


class AppStateConstants(Enum):
    PROJECT_DIRECTORY = 'project_directory'
    IMPORT_DIRECTORY = 'import_directory'
    TAB_DIRECTORIES = 'tab_directories'

    PRIMARY_IMAGE_PATH = 'primary_image_path'

    APP_STATUS = 'app_status'


class AppStatusConstants(Enum):
    IDLE = 'Idle'
    BUSY = 'Busy'


class AppNameConstants(Enum):
    APPLICATION_TITLE = 'Image Processing App'
