import os

from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

from models.image_thumbnail_tile_component_model import ImageThumbnailTileComponentModel
from menu.file_commands.import_image_command import ImportImageCommand


class ImageThumbnailTileComponent(QWidget):

    clicked = pyqtSignal(str)

    def __init__(self, image_path):
        super().__init__()

        self.model = ImageThumbnailTileComponentModel(image_path)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.thumbnail_label = QLabel()
        self.thumbnail_label.setFixedSize(100, 100)
        self.set_thumbnail(image_path)
        self.name_label = QLabel(os.path.basename(image_path))
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # self.setScaledContents(True)

        self.layout.addWidget(self.thumbnail_label)
        self.layout.addWidget(self.name_label)

    def set_thumbnail(self, image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.thumbnail_label.setPixmap(pixmap.scaled(
                self.thumbnail_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

    def mousePressEvent(self, event):
        # Обрабатываем клик ЛКМ
        super().mousePressEvent(event)
        print('ПОЛЕТЕЛ',self.model.image_path)
        self.clicked.emit(self.model.image_path)
