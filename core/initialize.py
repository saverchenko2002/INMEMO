from core.controller_registry import ControllerRegistry

from menu.commands.command_classes.file_command import FileCommand
from controllers.menu_controllers.file_controller import FileController

from menu.commands.command_classes.edit_command import EditCommand
from controllers.menu_controllers.edit_controller import EditController

from menu.commands.command_classes.filters_command import FiltersCommand
from controllers.menu_controllers.filters_controller import FiltersController

from ui.command_classes.tabs_component_command import TabsComponentCommand
from controllers.component_controllers.tabs_component_controller import TabsComponentController

from ui.command_classes.image_thumbnail_tile_component_command import ImageThumbnailTileComponentCommand
from controllers.component_controllers.image_thumbnail_tile_component_controller import ImageThumbnailTileComponentController

from menu.commands.command_classes.contours_command import ContoursCommand
from controllers.menu_controllers.contours_controller import ContoursController

from menu.commands.command_classes.preprocess_command import PreprocessCommand
from controllers.menu_controllers.preprocess_controller import PreprocessController

from core.app_state_service import AppStateService


def register_controllers():
    ControllerRegistry.register(FileCommand, FileController())
    ControllerRegistry.register(EditCommand, EditController())
    ControllerRegistry.register(FiltersCommand, FiltersController())
    ControllerRegistry.register(ContoursCommand, ContoursController())
    ControllerRegistry.register(PreprocessCommand, PreprocessController())

    ControllerRegistry.register(ImageThumbnailTileComponentCommand, ImageThumbnailTileComponentController())
    ControllerRegistry.register(TabsComponentCommand, TabsComponentController())


def initialize_services():
    AppStateService()
