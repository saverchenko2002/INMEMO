from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt


from models.thumbnail_listview_component_model import ThumbnailListviewComponentModel

from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component import ImageThumbnailTileComponent

from schema.ImageModel import ImageModel

class ThumbnailListviewComponent(QWidget):

    list_item_clicked = pyqtSignal(str)

    def __init__(self, images: list[ImageModel]):
        super().__init__()
        self.model = ThumbnailListviewComponentModel(images)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: 0px; }")
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.list_widget = QWidget()
        self.list_layout = QVBoxLayout(self.list_widget)
        self.list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.list_widget)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

        self.create_listview()

    def create_listview(self):
        for image in self.model.images:
            self.add_tile(image)

    def add_tile(self, image):
        thumbnail = ImageThumbnailTileComponent(image)
        thumbnail.clicked.connect(self.on_tile_clicked)
        self.list_layout.addWidget(thumbnail)

    def add_tile_model(self, image):
        self.model.images.append(image)
        self.add_tile(image)

    def update_tile(self, image):
        for i in range(self.list_layout.count()):
            widget = self.list_layout.itemAt(i).widget()
            if widget.model.current_image_path == image.current_image_path:
                widget.set_thumbnail(image.current_image_path)
                break

    def remove_tile(self, image):
        for i in range(self.list_layout.count()):
            widget = self.list_layout.itemAt(i).widget()
            if widget.model.current_image_path == image.current_image_path:
                self.list_layout.removeWidget(widget)
                widget.deleteLater()
                break

        self.model.images = [img for img in self.model.images if img.current_image_path != image.current_image_path]

    def rename_tile(self, image):
        count = self.list_layout.count()
        for i in range(count):
            item = self.list_layout.itemAt(i)

            widget = item.widget()
            if widget.model.original_image_path == image.original_image_path:
                widget.update_tile_name(image.current_image_path)
                break

    def update_listview(self, images):
        self.model.images.extend(images)

        for image_path in images:
            self.add_tile(image_path)

    def on_tile_clicked(self, image_path):
        self.list_item_clicked.emit(image_path)
