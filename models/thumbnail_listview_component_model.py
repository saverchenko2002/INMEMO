from models.base_component_model import BaseComponentModel
from schema.ImageModel import ImageModel

class ThumbnailListviewComponentModel(BaseComponentModel):
    def __init__(self, images: list[ImageModel]):
        self.images = images
