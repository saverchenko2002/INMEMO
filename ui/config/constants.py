from enum import Enum
from enum import StrEnum


import cv2


class FileSystemControlFlags(StrEnum):
    REMOVE_F = 'REMOVE'
    ADD_F = 'ADD'
    RENAME_F = 'RENAME'
    MOVE_F = 'MOVE'
    NONE_F = 'NONE'


class DragDropConstants(Enum):
    TAB_DIRECTORY = 'tab_dir'
    IMAGE_PATH = 'image_path'

class MoveToTabConstants(Enum):
    TARGET_FOLDER_NAME = 'target_folder_name'
    SOURCE_IMAGE_PATH = 'source_image_path'

class RemoveTabConstants(Enum):
    REMOVE_TAB_NAME = 'remove_tab_name'

class ChangeTabConstants(Enum):
    CHANGE_TAB_NAME = 'change_tab_name'

class ChangeImageNameConstants(Enum):
    IMAGE_MODEL = 'image_model'

class OperationConstants(Enum):
    OPERATION_HEADER = 'Image Operations'
    CONTROL_COMMAND = 'Swap Images'
    ADD_OPERATION = 'Add'
    SUBTRACT_OPERATION = 'Subtract'
    OPERATION_OPERATOR = 'operation_operator'
    SOURCE_OPERAND = 'source_operand'
    TARGET_OPERAND = 'target_operand'
    IMAGE_PATH = 'image_path'

class ContoursWindow(Enum):
    WINDOW_HEADER = 'Параметры поиска контуров'

class ContoursChainMethods(Enum):
    CHAIN_APPROX_SIMPLE = cv2.CHAIN_APPROX_SIMPLE
    CHAIN_APPROX_NONE = cv2.CHAIN_APPROX_NONE
    CHAIN_APPROX_TC89_L1 = cv2.CHAIN_APPROX_TC89_L1
    CHAIN_APPROX_TC89_KCOS = cv2.CHAIN_APPROX_TC89_KCOS


class ContoursRetrieveOptions(Enum):
    RETR_EXTERNAL = cv2.RETR_EXTERNAL
    RETR_LIST = cv2.RETR_LIST
    RETR_TREE = cv2.RETR_TREE
    RETR_CCOMP = cv2.RETR_CCOMP
    RETR_FLOODFILL = cv2.RETR_FLOODFILL



# class TilesInteractionConstants(Enum)
