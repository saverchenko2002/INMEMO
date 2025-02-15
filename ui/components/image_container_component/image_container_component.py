from utils.decorators.state_subscribe_decorator import state_model_subscribe

from models.image_container_component_model import ImageContainerComponentModel

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


@state_model_subscribe
class ImageContainerComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = ImageContainerComponentModel()

        self.image_label = QLabel('Изображение не загружено')
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def react_state_update(self, key, value):
        print('ключ БАЛЯТЬ) ', key)
        self.model[key] = value
        self.set_image(value)

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(
            self.width(), self.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.FastTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)

        self.setMinimumSize(scaled_pixmap.width(), scaled_pixmap.height())
