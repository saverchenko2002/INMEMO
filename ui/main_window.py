from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

from menu.menu_bar import MenuBar
from core.command_publisher import CommandPublisher
from core.command_executor import CommandExecutor


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        menu_bar = MenuBar(self)
        self.setMenuBar(menu_bar)

        CommandPublisher.subscribe(self)

        self.setWindowTitle("Image Processing App")

        layout = QVBoxLayout()
        label = QLabel("Добро пожаловать в приложение!")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def close_event(self, event):
        CommandPublisher.unsubscribe(self)
        print('amogus')

    @staticmethod
    def on_command_received(command):
        print('ZZZZZZZZZZZ')
        print(command)
        CommandExecutor.execute(command)


