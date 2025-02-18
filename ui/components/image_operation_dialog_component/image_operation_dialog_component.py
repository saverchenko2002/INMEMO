import logging

from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QSizePolicy, QDialogButtonBox
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap

from ui.config.constants import OperationConstants


class ImageOperationDialogComponent(QDialog):

    operation_completed = pyqtSignal(dict)

    def __init__(self, source_image_path, target_image_path):
        super().__init__()

        self.setFixedSize(QApplication.primaryScreen().size().width() // 4, QApplication.primaryScreen().size().height() // 4)
        self.setWindowTitle(OperationConstants.OPERATION_HEADER.value)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        main_layout = QVBoxLayout(self)

        commands_layout = QHBoxLayout()
        images_layout = QHBoxLayout()

        self.swap_button = QPushButton(OperationConstants.CONTROL_COMMAND.value)
        self.swap_button.clicked.connect(self.swap_images)

        commands_layout.addWidget(self.swap_button)

        self.source_image = QLabel(self)
        self.set_thumbnail(source_image_path, self.source_image)
        self.target_image = QLabel(self)
        self.set_thumbnail(target_image_path, self.target_image)

        self.source_image.setScaledContents(True)
        self.target_image.setScaledContents(True)

        main_layout.addLayout(commands_layout)

        self.operation_combo = QComboBox(self)
        self.operation_combo.addItem(OperationConstants.ADD_OPERATION.value, OperationConstants.ADD_OPERATION.name)
        self.operation_combo.addItem(OperationConstants.SUBTRACT_OPERATION.value, OperationConstants.SUBTRACT_OPERATION.name)

        images_layout.addWidget(self.source_image)
        images_layout.addWidget(self.operation_combo)
        images_layout.addWidget(self.target_image)

        main_layout.addLayout(images_layout)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        main_layout.addWidget(self.button_box)

    def accept(self):
        self.operation_completed.emit(self._construct_payload())
        super().accept()

    def _construct_payload(self):
        return {
            OperationConstants.OPERATION_OPERATOR.value: self.operation_combo.currentText(),
            OperationConstants.SOURCE_OPERAND.value: self.source_image.property(OperationConstants.IMAGE_PATH.value),
            OperationConstants.TARGET_OPERAND.value: self.target_image.property(OperationConstants.IMAGE_PATH.value)
        }

    def reject(self):
        super().reject()

    def set_thumbnail(self, image_path, label):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            label.setPixmap(pixmap)
            label.setProperty(OperationConstants.IMAGE_PATH.value, image_path)

    def swap_images(self):
        source_image_pixmap = self.source_image.pixmap()
        target_image_pixmap = self.target_image.pixmap()

        source_image_path = self.source_image.property(OperationConstants.IMAGE_PATH.value)
        target_image_path = self.target_image.property(OperationConstants.IMAGE_PATH.value)

        self.source_image.setPixmap(target_image_pixmap)
        self.target_image.setPixmap(source_image_pixmap)

        self.source_image.setProperty(OperationConstants.IMAGE_PATH.value, target_image_path)
        self.target_image.setProperty(OperationConstants.IMAGE_PATH.value, source_image_path)