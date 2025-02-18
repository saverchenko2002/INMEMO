from PyQt6.QtWidgets import QApplication, QDialog, QSizePolicy, QVBoxLayout, QHBoxLayout, QComboBox, QDialogButtonBox

from ui.config.constants import ContoursWindow


class ComboEnumDialogComponent(QDialog):
    def __init__(self, enums_list):
        super().__init__()

        self.setFixedSize(QApplication.primaryScreen().size().width() // 4, QApplication.primaryScreen().size().height() // 16)
        self.setWindowTitle(ContoursWindow.WINDOW_HEADER.value)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.combos = []

        self.layout = QVBoxLayout(self)

        self.buttons_layout = QHBoxLayout()

        for enum in enums_list:
            combo = QComboBox(self)
            for item in enum:
                combo.addItem(item.name, item.value)
            self.combos.append(combo)
            self.buttons_layout.addWidget(combo)

        self.layout.addLayout(self.buttons_layout)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)



        self.layout.addWidget(button_box)

    def accept(self):
        super().accept()
        
    def reject(self):
        super().reject()

    def get_selections(self):
        selections = []
        for combo in self.combos:
            selections.append(combo.currentData())
        return selections
