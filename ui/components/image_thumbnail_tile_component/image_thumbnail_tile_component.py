import logging
import os
import json

from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QStyle, QMessageBox
from PyQt6.QtGui import QPixmap, QPainter, QDrag, QRegularExpressionValidator
from PyQt6.QtCore import Qt, QMimeData, pyqtSignal, QRegularExpression, QMetaObject, Q_ARG, QSize

from ui.config.constants import DragDropConstants

from ui.components.image_operation_dialog_component.image_operation_dialog_component import ImageOperationDialogComponent
from ui.config.constants import OperationConstants
from ui.config.constants import ImageModelConstants
from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.manipulate_images_command import ManipulateImagesCommand
from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.rename_image_command import RenameImageCommand
from ui.components.image_thumbnail_tile_component.image_thumbnail_tile_component_commands.remove_image_command import RemoveImageCommand
from schema.ImageModel import ImageModel

class ImageThumbnailTileComponent(QWidget):

    clicked = pyqtSignal(str)

    def __init__(self, model: ImageModel):
        super().__init__()

        self.model = model
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.thumbnail_label = QLabel()
        self.thumbnail_label.setFixedSize(100, 100)
        self.set_thumbnail(self.model.current_image_path)
        self.name_label = QLabel(os.path.basename(self.model.current_image_path))
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.name_edit = QLineEdit(os.path.basename(self.model.current_image_path))
        self.name_edit.setValidator(self._create_validator())
        self.name_edit.setVisible(False)

        self.info_layout = QVBoxLayout()
        self.info_layout.addWidget(self.name_label)
        self.info_layout.addWidget(self.name_edit)

        self.control_layout = QVBoxLayout()
        self.control_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        icon_size = QSize(
            self.style().pixelMetric(QStyle.PixelMetric.PM_SmallIconSize),
            self.style().pixelMetric(QStyle.PixelMetric.PM_SmallIconSize)
        )

        delete_button = QPushButton()
        delete_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_BrowserStop))
        delete_button.setFixedSize(icon_size)
        delete_button.clicked.connect(self._delete_tile)
        self.control_layout.addWidget(delete_button)

        info_button = QPushButton()
        info_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation))
        info_button.setFixedSize(icon_size)
        info_button.clicked.connect(self._show_object_info)
        self.control_layout.addWidget(info_button)

        self.layout.addWidget(self.thumbnail_label)
        self.layout.addLayout(self.info_layout)
        self.layout.addLayout(self.control_layout)

        self.setAcceptDrops(True)

        self.name_label.mouseDoubleClickEvent = self._enable_editing
        self.name_edit.editingFinished.connect(self._apply_name_change)

    def _create_validator(self):
        regex = r'^[\w,\s-]+\.(jpg|jpeg|png)$'
        return QRegularExpressionValidator(QRegularExpression(regex))

    def _show_object_info(self):
        obj_info = ""
        model_dict = self.model.dict()  # Получаем словарь атрибутов модели
        for attr, value in model_dict.items():
            if isinstance(value, dict):
                obj_info += f"<b>{attr}</b>:<br>"
                for sub_attr, sub_value in value.items():
                    obj_info += f"  <b>{sub_attr}</b>: {sub_value}<br>"
            else:
                obj_info += f"<b>{attr}</b>: {value}<br>"

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Информация об объекте")
        msg_box.setText(obj_info)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def _delete_tile(self):
        image_name = os.path.basename(self.model.original_image_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Подтверждение удаления")
        msg_box.setText(f"Вы уверены, что хотите удалить '{image_name}'?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        response = msg_box.exec()

        if response == QMessageBox.StandardButton.Yes:
            RemoveImageCommand(**{
                ImageModelConstants.IMAGE_MODEL.value: self.model
            })
            pass

    def _enable_editing(self, event):
        self.name_label.setVisible(False)
        self.name_edit.setVisible(True)

    def update_tile_name(self, name):
        if not self.name_label:  # Проверяем, что name_label существует
            logging.error("name_label is None")
            return  # Выход из функции, если name_label не существует

        logging.info(f"Updating tile name to: {name}")
        self.name_label.setText(os.path.basename(name))
        print('self.model in update tile name')
        print(self.model)
        self.model.original_image_path = name
        self.model.current_image_path = name
        logging.info(f"After updating name: {self.name_label}")
        print(self.model, 'Я ОБНОВЛЁН БРО')
    def _apply_name_change(self):
        new_name = self.name_edit.text().strip()
        if new_name and new_name != self.name_label.text():
            if self.name_edit.hasAcceptableInput():
                self.model.current_image_path = os.path.join(os.path.dirname(self.model.current_image_path), new_name)
                logging.info(self.model)
                print('new_name', new_name)
                self.name_label.setText(new_name)
                self.model.current_image_path = os.path.join(os.path.dirname(self.model.current_image_path), new_name)
                RenameImageCommand(**{
                    ImageModelConstants.IMAGE_MODEL.value: self.model
                })
            else:
                self.name_edit.setStyleSheet("border: 1px solid red;")
        self.name_label.setVisible(True)
        self.name_edit.setVisible(False)

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
            int(pixmap.width() // 1.3),
            int(pixmap.height() // 1.3),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        return scaled_pixmap

    def _construct_mime(self):
        data = {
            DragDropConstants.IMAGE_PATH.value: self.model.current_image_path,
            DragDropConstants.TAB_DIRECTORY.value: os.path.dirname(self.model.current_image_path)
        }

        serialized_data = json.dumps(data)

        mime_data = QMimeData()
        mime_data.setText(serialized_data)

        return mime_data

    def _deconstruct_mime(self, data):
        return json.loads(data)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print('ПОЛЕТЕЛ НАХУЙ', self.model.current_image_path)
        self.clicked.emit(self.model.current_image_path)

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
            if data[DragDropConstants.TAB_DIRECTORY.value] == os.path.dirname(self.model.current_image_path):
                dialog = ImageOperationDialogComponent(self.model.current_image_path, data[DragDropConstants.IMAGE_PATH.value])
                dialog.operation_completed.connect(self._handle_operation_result)
                dialog.exec()
                event.acceptProposedAction()
            elif data[DragDropConstants.TAB_DIRECTORY.value] != os.path.dirname(self.model.current_image_path):
                event.ignore()

    def _handle_operation_result(self, payload):
        logging.debug(payload)
        return ManipulateImagesCommand(**payload)
