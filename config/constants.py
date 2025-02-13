from enum import Enum


class AppStateConstants(Enum):
    PROJECT_DIRECTORY = 'project_directory'
    APP_STATUS = 'app_status'
    IMPORT_DIRECTORY = 'import_directory'
    TAB_DIRECTORIES = 'tab_directories'


class AppStatusConstants(Enum):
    IDLE = 'Idle'
    BUSY = 'Busy'


class AppNameConstants(Enum):
    APPLICATION_TITLE = 'Image Processing App'
