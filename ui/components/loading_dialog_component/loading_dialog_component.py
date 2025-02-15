from config.constants import AppNameConstants

from PyQt6.QtWidgets import QProgressDialog


class LoadingDialogComponent:
    def __init__(self, parent=None):
        self.progress_dialog = QProgressDialog('Загрузка...', None, 0, 0, parent)
        self.progress_dialog.setModal(True)
        self.progress_dialog.setWindowTitle(AppNameConstants.APPLICATION_TITLE.value)

    def show(self):
        self.progress_dialog.show()

    def set_message(self, message: str):
        self.progress_dialog.setLabel(message)

    def hide(self):
        self.progress_dialog.hide()
