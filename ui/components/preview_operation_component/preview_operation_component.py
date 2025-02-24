import os
from typing import Callable

from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QSlider, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
from cv2 import imread, IMREAD_GRAYSCALE

from controllers.utils import get_unique_filename, save_image
from ui.components.preview_operation_component.fields_constraints import OperationField


class PreviewOperationComponent(QDialog):
    def __init__(self, title: str, image_path: str, method_func: Callable, params: list[OperationField]):
        super().__init__()

        self.params = params
        self.method_func = method_func
        self.image_path = image_path
        self.method_func = method_func
        self.new_file_path = None

        self.setFixedSize(QApplication.primaryScreen().size().width() // 2,
                          QApplication.primaryScreen().size().height() // 2)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setWindowTitle(title)

        self.preview_layout = QVBoxLayout()

        self.source_image = QLabel(self)
        self.source_image.setScaledContents(True)
        source_image_data, pixmap = self._get_pixmap_data_from_path(image_path)
        self.source_image_data = source_image_data
        self.source_image.setPixmap(pixmap)

        self.target_image = QLabel(self)
        self.target_image.setScaledContents(True)
        self.target_image_data = self._get_method_data()
        self.target_image.setPixmap(self._get_pixmap_data_from_data(self.target_image_data))

        self.preview_layout.addWidget(self.source_image)
        self.preview_layout.addWidget(self.target_image)

        self.parameters_layout = QVBoxLayout()
        self.parameters_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._init_parameters(self.parameters_layout, self.params)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self._accept)
        self.button_box.rejected.connect(self._reject)

        self.layout = QHBoxLayout(self)
        self.layout.addLayout(self.preview_layout, 6)
        self.layout.addLayout(self.parameters_layout, 4)
        self.parameters_layout.addWidget(self.button_box)

    def get_new_file_path(self):
        return self.new_file_path

    def _perform_save(self):
        dir_ = os.path.dirname(self.image_path)
        filename = os.path.basename(self.image_path)
        name, ext = os.path.splitext(filename)
        new_filename = os.path.join(dir_, f'{name}_{self.method_func.__name__}_{ext}')
        new_filename = get_unique_filename(new_filename)
        print(new_filename)
        self.new_file_path = save_image(new_filename, self.target_image_data)

    def _get_method_data(self):
        current_values = [param.current_value for param in self.params]
        current_values.insert(0, self.source_image_data)
        return self.method_func(*tuple(current_values))

    def _accept(self):
        self._perform_save()
        super().accept()

    def _reject(self):
        super().reject()

    def _init_parameters(self, params_layout: QVBoxLayout, params: list[OperationField]):
        for param in params:
            label = QLabel(f'{param.param_name}: {str(param.default_value)}')
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            params_layout.addWidget(label)
            match  param.field_type:
                case param.field_type.RANGE:
                    slider = QSlider(Qt.Orientation.Horizontal)
                    steps = (param.max_value - param.min_value) // param.step
                    slider.setRange(0, steps)
                    slider.setValue((param.default_value - param.min_value) // param.step)
                    slider.valueChanged.connect(
                        lambda value, _param=param, _label=label, _slider=slider: [
                            _label.setText(f'{_param.param_name}: {_param.min_value + _param.step * _slider.value()}'),
                            setattr(_param, 'current_value', _param.min_value + _param.step * _slider.value()),
                            self.target_image.setPixmap(self._get_pixmap_data_from_data(self._get_method_data()))
                        ]
                    )
                    params_layout.addWidget(slider)
                case param.field_type.CHECKBOX:
                    checkbox = QCheckBox(param.param_name)
                    if param.default_value:
                        checkbox.setChecked(True)
                    params_layout.addWidget(checkbox)
                    checkbox.stateChanged.connect(
                        lambda value, _param=param, _label=label, _checkbox=checkbox: [
                            _label.setText(f'{_param.param_name}: {_checkbox.isChecked()}'),
                            setattr(_param, 'current_value', _checkbox.isChecked()),
                            self.target_image.setPixmap(self._get_pixmap_data_from_data(self._get_method_data()))
                        ]
                    )

    def _get_pixmap_data_from_data(self, image_data: []):
        height, width = image_data.shape
        bytes_per_line = width

        return QPixmap(QImage(image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8))

    def _get_pixmap_data_from_path(self, image_path: str):
        image_data = imread(image_path, IMREAD_GRAYSCALE)

        height, width = image_data.shape
        bytes_per_line = width

        return (image_data,
                QPixmap(QImage(image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)))
