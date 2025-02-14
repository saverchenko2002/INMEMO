from core.app_state_service import AppStateService

from models.image_container_component_model import ImageContainerComponentModel

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class ImageContainerComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = ImageContainerComponentModel()

        for field in vars(self.model).keys():
            print(f'подписались ежжи по полю{field}')
            print(self)
            AppStateService().subscribe(field, self)

        self.image_label = QLabel('Изображение не загружено')
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(True)
        #self.image_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def react_state_update(self, key, value):
        self.model[key] = value
        print('ты живой??', value)
        self.set_image(value)

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     self.update()
    #
    # def update_image_on_resize(self):
    #     if self.pixmap:
    #         scaled_pixmap = self.pixmap.scaled(
    #             self.width(), self.height(),
    #             Qt.AspectRatioMode.KeepAspectRatio,
    #             Qt.TransformationMode.SmoothTransformation
    #         )
    #         self.image_label.setPixmap(scaled_pixmap)

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(
            self.width(), self.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.FastTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)
        # self.update_image_on_resize()
        # pixmap = QPixmap(image_path)
        # scaled_pixmap = pixmap.scaled(self.width(), self.height(), Qt.AspectRatioMode.KeepAspectRatio)
        # self.image_label.setPixmap(scaled_pixmap)





