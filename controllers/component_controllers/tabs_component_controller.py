from core.base.controller import Controller
from core.app_state_service import AppStateService

from utils.decorators.app_status_decorator import with_app_status_change

from config.constants import AppStateConstants

from ui.components.tabs_component.tabs_component_commands.change_primary_image_command import ChangePrimaryImageCommand


class TabsComponentController(Controller):
    def __init__(self):
        super().__init__()

        self.add_handler(ChangePrimaryImageCommand, self.handle_change_primary_image)

    def handle_change_primary_image(self, command):
        primary_image_path = AppStateService().get_state(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        input_primary_image_path = command.__dict__.get(AppStateConstants.PRIMARY_IMAGE_PATH.value)
        if primary_image_path != input_primary_image_path:
            AppStateService().set_state(AppStateConstants.PRIMARY_IMAGE_PATH.value, input_primary_image_path)


