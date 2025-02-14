from PyQt6.QtWidgets import QWidget, QVBoxLayout

from models.thumbnail_listview_component_model import ThumbnailListviewComponentModel

from ui.components.image_thumbnail_tile_component import ImageThumbnailTileComponent


class ThumbnailListviewComponent(QWidget):
    def __init__(self, images):
        super().__init__()

        self.model = ThumbnailListviewComponentModel(images)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.create_listview()

    def create_listview(self):
        print('ВСЕ НА МЕСТЕ СПОРТСМЕНЫ')
        print(self.model.images)
        for image_path in self.model.images:
            self.add_tile(image_path)

    def add_tile(self, image_path):
        thumbnail = ImageThumbnailTileComponent(image_path)
        self.layout.addWidget(thumbnail)

    def update_listview(self, images):
        print("Обновление списка плиток. Новые изображения:", images)
        self.model.images = self.model.images.union(images)

        for image_path in images:
            self.add_tile(image_path)
        # self.clear_listview()
        # self.model.images = images
        # self.create_listview()

    def clear_listview(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
