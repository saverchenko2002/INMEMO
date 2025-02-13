from config.constants import AppStatusConstants
from models.base_component_model import BaseComponentModel


class AppStatusComponentModel(BaseComponentModel):

    def __init__(self):
        self.app_status = AppStatusConstants.IDLE
