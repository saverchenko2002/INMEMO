from core.app_state_service import AppStateService

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


from models.directory_component_model import DirectoryComponentModel


class DirectoryComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = DirectoryComponentModel()

        self.directory_label = QLabel(self.model.project_directory)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.directory_label)
        self.setLayout(self.layout)

        for field in vars(self.model).keys():
            print(f'подписались ежжи по полю{field}')
            print(self)
            AppStateService().subscribe(field, self)

    def react_state_update(self, key):
        print('DirectoryComponentModel сначала я получаю доступ')
        state = AppStateService().get_state()
        print('DirectoryComponentModel сначала я получаю доступ')
        self.model.project_directory = AppStateService().get_state()[key]
        self.directory_label.setText(self.model.project_directory)
