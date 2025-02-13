from core.controller_registry import ControllerRegistry

from menu.command.file_command import FileCommand
from menu.command.edit_command import EditCommand

from controllers.menu_controllers.file_controller import FileController
from controllers.menu_controllers.edit_controller import EditController

from core.app_state_service import AppStateService


def register_controllers():
    ControllerRegistry.register(FileCommand, FileController())
    ControllerRegistry.register(EditCommand, EditController())


def initialize_services():
    AppStateService()
