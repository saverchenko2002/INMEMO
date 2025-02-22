import os

from PyQt6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QSlider, QLabel, QCheckBox, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

from controllers.utils import get_unique_filename, save_image

from processing.image.methods.edges import canny_method
from processing.image.utils import read_grayscale
import cv2

class CannyPreviewComponent(QDialog):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

        self.setFixedSize(QApplication.primaryScreen().size().width() // 2,
                          QApplication.primaryScreen().size().height() // 2)
        self.setWindowTitle('Canny Edges Detection Preview')
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.preview_layout = QVBoxLayout()

        self.source_image = QLabel(self)
        self.source_image.setScaledContents(True)
        self.source_image_data = read_grayscale(image_path)
        print(type(self.source_image_data), self.source_image_data.dtype, self.source_image_data.shape)

        height, width = self.source_image_data.shape
        bytes_per_line = width
        self.source_image.setPixmap(
            QPixmap(QImage(self.source_image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)))




        self.parameters_layout = QVBoxLayout()
        self.parameters_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.default_threshold1_value = 100
        self.threshold1_slider = QSlider(Qt.Orientation.Horizontal)
        self.threshold1_slider.setMinimum(0)
        self.threshold1_slider.setMaximum(255)
        self.threshold1_slider.setValue(self.default_threshold1_value)
        self.threshold1_slider.valueChanged.connect(self.handle_threshold1_change)
        self.threshold1_slider.sliderReleased.connect(self.handle_threshold1_change)

        self.threshold1_slider_value_label = QLabel(f'threshold1: {str(self.default_threshold1_value)}')
        self.threshold1_slider_value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.default_threshold2_value = 200
        self.threshold2_slider = QSlider(Qt.Orientation.Horizontal)
        self.threshold2_slider.setMinimum(0)
        self.threshold2_slider.setMaximum(255)
        self.threshold2_slider.setValue(self.default_threshold2_value)
        self.threshold2_slider.valueChanged.connect(self.handle_threshold2_change)
        self.threshold2_slider.sliderReleased.connect(self.handle_threshold2_change)

        self.threshold2_slider_value_label = QLabel(f'threshold2: {str(self.default_threshold2_value)}')
        self.threshold2_slider_value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.aperture_size_min_val = 3
        self.aperture_size_max_val = 7
        self.aperture_size_step = 2

        self.aperture_size_slider = QSlider(Qt.Orientation.Horizontal)
        steps = (self.aperture_size_max_val - self.aperture_size_min_val) // self.aperture_size_step
        self.aperture_size_slider.setRange(0, steps)

        self.aperture_size_slider.setValue(0)
        self.aperture_size_slider.valueChanged.connect(self.handle_aperture_size_change_visual)
        self.aperture_size_slider.sliderReleased.connect(self.handle_aperture_size_change)

        self.aperture_slider_value_label = QLabel(f'aperture_size: {str(self.aperture_size_min_val)}')
        self.aperture_slider_value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.l2gradient_checkbox = QCheckBox("L2gradient")
        self.l2gradient_checkbox.stateChanged.connect(self.l2gradient_checkbox_change)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.parameters_layout.addWidget(self.threshold1_slider_value_label)
        self.parameters_layout.addWidget(self.threshold1_slider)

        self.parameters_layout.addWidget(self.threshold2_slider_value_label)
        self.parameters_layout.addWidget(self.threshold2_slider)

        self.parameters_layout.addWidget(self.aperture_slider_value_label)
        self.parameters_layout.addWidget(self.aperture_size_slider)

        self.parameters_layout.addWidget(self.l2gradient_checkbox)

        self.parameters_layout.addWidget(self.button_box)

        self.layout = QHBoxLayout(self)

        self.preview_layout.addWidget(self.source_image, 5)

        self.target_image = QLabel(self)
        self.target_image.setScaledContents(True)
        self.target_image_data = canny_method(*self.get_canny_data())

        height, width = self.target_image_data.shape
        bytes_per_line = width
        self.target_image.setPixmap(
            QPixmap(QImage(self.target_image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)))

        self.preview_layout.addWidget(self.target_image)



        self.layout.addLayout(self.preview_layout, 6)
        self.layout.addLayout(self.parameters_layout, 4)

        self.new_file_path = None

    def get_new_file_path(self):
        return self.new_file_path

    def accept(self):
        self._perform_save()
        super().accept()

    def _perform_save(self):
        dir_ = os.path.dirname(self.image_path)
        filename = os.path.basename(self.image_path)
        name, ext = os.path.splitext(filename)
        new_filename = os.path.join(dir_, f'{name}_CANNY{ext}')
        new_filename = get_unique_filename(new_filename)
        self.new_file_path = save_image(new_filename, self.target_image_data)

    def reject(self):
        super().reject()

    def handle_threshold1_change_visual(self):
        self.threshold1_slider_value_label.setText(f'threshold1: {str(self.threshold1_slider.value())}')

    def handle_threshold1_change(self):
        self.threshold1_slider_value_label.setText(f'threshold1: {str(self.threshold1_slider.value())}')
        self.target_image_data = canny_method(*self.get_canny_data())
        height, width = self.target_image_data.shape
        bytes_per_line = width
        self.target_image.setPixmap(
            QPixmap(QImage(self.target_image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)))

    def handle_threshold2_change_visual(self):
        self.threshold2_slider_value_label.setText(f'threshold2: {str(self.threshold2_slider.value())}')

    def handle_threshold2_change(self):
        self.threshold2_slider_value_label.setText(f'threshold2: {str(self.threshold2_slider.value())}')
        self.target_image_data = canny_method(*self.get_canny_data())
        height, width = self.target_image_data.shape
        bytes_per_line = width
        self.target_image.setPixmap(
            QPixmap(QImage(self.target_image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)))

    def handle_aperture_size_change_visual(self, value):
        actual_value = self.aperture_size_min_val + value * self.aperture_size_step
        self.aperture_slider_value_label.setText(f'aperture_size: {str(actual_value)}')

    def handle_aperture_size_change(self):
        actual_value = self.aperture_size_min_val + self.aperture_size_slider.value() * self.aperture_size_step

        self.aperture_slider_value_label.setText(f'aperture_size: {str(actual_value)}')
        self.target_image_data = canny_method(*self.get_canny_data())
        height, width = self.target_image_data.shape
        bytes_per_line = width
        self.target_image.setPixmap(
            QPixmap(QImage(self.target_image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)))

    def l2gradient_checkbox_change(self, state):
        self.target_image_data = canny_method(*self.get_canny_data())
        height, width = self.target_image_data.shape
        bytes_per_line = width
        self.target_image.setPixmap(
            QPixmap(QImage(self.target_image_data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)))

    def get_canny_data(self):
        return (self.image_path,
                float(self.threshold1_slider.value()),
                float(self.threshold2_slider.value()),
                self.aperture_size_min_val + self.aperture_size_slider.value() * self.aperture_size_step,
                self.l2gradient_checkbox.isChecked())
