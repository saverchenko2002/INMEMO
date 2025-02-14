from models.base_component_model import BaseComponentModel


class ImageThumbnailTileComponentModel(BaseComponentModel):
    def __init__(self, image_path):
        self.image_path = image_path
