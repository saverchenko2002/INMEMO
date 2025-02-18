import logging
import os
import json

from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QDrag
from PyQt6.QtCore import Qt, QMimeData, pyqtSignal

from models.image_thumbnail_tile_component_model import ImageThumbnailTileComponentModel

from ui.config.constants import DragDropConstants

from ui.components.image_operation_dialog_component.image_operation_dialog_component import ImageOperationDialogComponent
from ui.config.constants import OperationConstants
from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.manipulate_images_command import ManipulateImagesCommand


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

    def _get_pixmap_for_drag(self):
        pixmap = QPixmap(self.size())
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setOpacity(0.5)
        self.render(painter)
        painter.end()

        scaled_pixmap = pixmap.scaled(
            pixmap.width() // 1.3,
            pixmap.height() // 1.3,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        return scaled_pixmap

    def _construct_mime(self):
        data = {
            DragDropConstants.IMAGE_PATH.value: self.model.image_path,
            DragDropConstants.TAB_DIRECTORY.value: os.path.dirname(self.model.image_path)
        }

        serialized_data = json.dumps(data)

        mime_data = QMimeData()
        mime_data.setText(serialized_data)

        return mime_data

    def _deconstruct_mime(self, data):
        return json.loads(data)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        self.clicked.emit(self.model.image_path)

        self.setVisible(False)

        drag = QDrag(self)
        drag.setMimeData(self._construct_mime())
        drag.setPixmap(self._get_pixmap_for_drag())
        drag.setHotSpot(event.pos())

        result = drag.exec(Qt.DropAction.MoveAction)
        self.setVisible(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasText():

            data = self._deconstruct_mime(event.mimeData().text())
            if data[DragDropConstants.TAB_DIRECTORY.value] == os.path.dirname(self.model.image_path):
                dialog = ImageOperationDialogComponent(self.model.image_path, data[DragDropConstants.IMAGE_PATH.value])
                dialog.operation_completed.connect(self._handle_operation_result)
                dialog.exec()
                event.acceptProposedAction()
            elif data[DragDropConstants.TAB_DIRECTORY.value] != os.path.dirname(self.model.image_path):
                event.ignore()

    def _handle_operation_result(self, payload):
        logging.debug(payload)
        return ManipulateImagesCommand(**payload)
