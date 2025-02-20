from core.base.command import Command
from ui.command_classes.image_thumbnail_tile_component_command import ImageThumbnailTileComponentCommand


class RemoveImageCommand(Command, ImageThumbnailTileComponentCommand):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.notify_observers()
        pass

    def execute(self):
        self.notify_observers()
