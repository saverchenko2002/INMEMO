from config.constants import AppStateConstants, AppStatusConstants

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from ui.components.loading_dialog_component.loading_dialog_component import LoadingDialogComponent

from models.app_status_component_model import AppStatusComponentModel

from utils.decorators.state_subscribe_decorator import state_model_subscribe


@state_model_subscribe
class AppStatusComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.loading_component = None

        self.model = AppStatusComponentModel()

        self.app_status = QLabel(self.model.app_status.value)

        self.app_status.setWordWrap(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.app_status)
        self.setLayout(self.layout)

        self.setStyleSheet("border: 1px solid blue;")

    def react_state_update(self, key, value):
        self.model[key] = value
        self.app_status.setText(self.model[key])

        if key == AppStateConstants.APP_STATUS.value:
            if value == AppStatusConstants.BUSY.value:
                if self.loading_component is None:
                    self.loading_component = LoadingDialogComponent()
                self.loading_component.show()
            else:
                self.loading_component.hide()
