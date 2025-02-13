from core.app_state_service import AppStateService

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


from models.app_status_component_model import AppStatusComponentModel


class AppStatusComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = AppStatusComponentModel()

        self.app_status = QLabel(self.model.app_status)

        self.app_status.setWordWrap(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.app_status)
        self.setLayout(self.layout)

        self.setStyleSheet("border: 1px solid blue;")

        for field in vars(self.model).keys():
            print(f'подписались ежжи по полю{field}')
            print(self)
            AppStateService().subscribe(field, self)

    def react_state_update(self, key, value):
        print(key)
        print(value)
        print('DirectoryComponentModel сначала я получаю доступ')
        print('DirectoryComponentModel сначала я получаю доступ')
        self.model[key] = value
        self.app_status.setText(self.model[key])
