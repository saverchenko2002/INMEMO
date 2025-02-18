from enum import Enum


class DragDropConstants(Enum):
    TAB_DIRECTORY = 'tab_dir'
    IMAGE_PATH = 'image_path'

class MoveToTabConstants(Enum):
    TARGET_FOLDER_NAME = 'target_folder_name'
    SOURCE_IMAGE_PATH = 'source_image_path'

class OperationConstants(Enum):
    OPERATION_HEADER = 'Image Operations'
    CONTROL_COMMAND = 'Swap Images'
    ADD_OPERATION = 'Add'
    SUBTRACT_OPERATION = 'Subtract'
    OPERATION_OPERATOR = 'operation_operator'
    SOURCE_OPERAND = 'source_operand'
    TARGET_OPERAND = 'target_operand'
    IMAGE_PATH = 'image_path'
# class TilesInteractionConstants(Enum)
