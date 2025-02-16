from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt


from models.thumbnail_listview_component_model import ThumbnailListviewComponentModel

from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component import ImageThumbnailTileComponent


class ThumbnailListviewComponent(QWidget):

    list_item_clicked = pyqtSignal(str)

    def __init__(self, images):
        super().__init__()

        self.model = ThumbnailListviewComponentModel(images)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: 0px; }")
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Создаем QWidget, который будет контейнером для всех элементов
        self.list_widget = QWidget()
        self.list_layout = QVBoxLayout(self.list_widget)
        self.list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Устанавливаем list_widget как содержимое для scroll_area
        self.scroll_area.setWidget(self.list_widget)

        # Основной layout для ThumbnailListviewComponent
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

        self.create_listview()

    def create_listview(self):
        # Добавляем элементы в layout прокручиваемой области
        for image_path in self.model.images:
            self.add_tile(image_path)

    def add_tile(self, image_path):
        thumbnail = ImageThumbnailTileComponent(image_path)
        thumbnail.clicked.connect(self.on_tile_clicked)
        self.list_layout.addWidget(thumbnail)

    def update_listview(self, images):
        # Обновляем модель изображений и добавляем новые элементы
        self.model.images = self.model.images.union(images)

        for image_path in images:
            self.add_tile(image_path)

    def on_tile_clicked(self, image_path):
        self.list_item_clicked.emit(image_path)