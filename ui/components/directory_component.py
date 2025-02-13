from core.app_state_service import AppStateService

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices

from models.directory_component_model import DirectoryComponentModel


class DirectoryComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = DirectoryComponentModel()
        self.directory_label = QLabel(self.model.project_directory)
        self.directory_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.directory_label)
        self.setLayout(self.layout)

        self.setStyleSheet("border: 1px solid blue;")


        for field in vars(self.model).keys():
            print(f'подписались ежжи по полю{field}')
            print(self)
            AppStateService().subscribe(field, self)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.model.project_directory))

    def react_state_update(self, key, value):
        print(key)
        print(value)
        print('DirectoryComponentModel сначала я получаю доступ')
        print('DirectoryComponentModel сначала я получаю доступ')
        self.model[key] = value
        self.directory_label.setText(self.model[key])
