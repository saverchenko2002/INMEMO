from models.base_component_model import BaseComponentModel


class ThumbnailListviewComponentModel(BaseComponentModel):
    def __init__(self, images):
        self.images = images
