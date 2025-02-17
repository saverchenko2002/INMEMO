import os

from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QDrag
from PyQt6.QtCore import Qt, QMimeData, pyqtSignal

from models.image_thumbnail_tile_component_model import ImageThumbnailTileComponentModel


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

        self.setAcceptDrops(True)

    def set_thumbnail(self, image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.thumbnail_label.setPixmap(pixmap.scaled(
                self.thumbnail_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        # Ваш код, который обрабатывает клик
        print('ПОЛЕТЕЛ', self.model.image_path)
        self.clicked.emit(self.model.image_path)

        # Скрываем текущий виджет перед началом перетаскивания
        self.setVisible(False)

        # Создаем MIME-данные для перетаскивания
        mime_data = QMimeData()
        mime_data.setText(self.model.image_path)  # Передаем путь изображения

        # Настроим drag объект

        pixmap = QPixmap(self.size())
        pixmap.fill(Qt.GlobalColor.transparent)  # Заливаем прозрачным фоном

        # Создаем QPainter и рисуем в pixmap с учетом прозрачности
        painter = QPainter(pixmap)
        painter.setOpacity(0.5)  # Устанавливаем уровень прозрачности (0.0 - полностью прозрачный, 1.0 - непрозрачный)
        self.render(painter)  # Рендерим содержимое виджета в pixmap
        painter.end()

        scaled_pixmap = pixmap.scaled(pixmap.width() // 1.3, pixmap.height() // 1.3,
                                      Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)

        # Настроим drag объект
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setPixmap(scaled_pixmap)
        drag.setHotSpot(event.pos())

        # Начинаем перетаскивание
        result = drag.exec(Qt.DropAction.MoveAction)

        # Если перетаскивание завершилось перемещением (или отменой), показываем исходный объект
        if result != Qt.DropAction.MoveAction:
            self.setVisible(True)  # Показываем исходный объект снова

    def dragEnterEvent(self, event: QDragEnterEvent):
        print('dragEnterEvent йооооу')
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        print('dragMoveEvent йооооу')
        event.accept()

    def dropEvent(self, event: QDropEvent):
        print("Dropped on component:", self.model.image_path)
        # Handle the drop here, e.g., initiate some action between the two components
        event.acceptProposedAction()