from models.base_component_model import BaseComponentModel


class TabsComponentModel(BaseComponentModel):
    def __init__(self):
        self.tab_images_map = {}
        self.primary_tab = str()
