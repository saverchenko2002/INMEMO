from core.controller_registry import ControllerRegistry

from menu.command_classes.file_command import FileCommand
from controllers.menu_controllers.file_controller import FileController

from menu.command_classes.edit_command import EditCommand
from controllers.menu_controllers.edit_controller import EditController

from ui.command_classes.tabs_component_command import TabsComponentCommand
from controllers.component_controllers.tabs_component_controller import TabsComponentController

from core.app_state_service import AppStateService


def register_controllers():
    ControllerRegistry.register(FileCommand, FileController())
    ControllerRegistry.register(EditCommand, EditController())

    ControllerRegistry.register(TabsComponentCommand, TabsComponentController())


def initialize_services():
    AppStateService()
