from pydantic import BaseModel, Field


from ui.config.constants import FileSystemControlFlags


class ImageModel(BaseModel):
    original_image_path: str = Field(default_factory=lambda: 'default')
    current_image_path: str

    filesystem_flag: FileSystemControlFlags = FileSystemControlFlags.NONE_F

    def model_post_init(self, __context):
        self.original_image_path = self.current_image_path
