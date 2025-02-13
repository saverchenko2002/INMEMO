from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

from models.pwd_model import PwdModel


class PwdComponent(QWidget):
    def __init__(self, model: PwdModel, parent=None):
        super().__init__(parent)
        self.model = model

        self.layout = QHBoxLayout()
        self.label = QLabel(self.model.directory)

        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
