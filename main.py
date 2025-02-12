import sys
from PyQt6.QtWidgets import QApplication

from core.initialize import register_controllers

from ui.main_window import MainWindow


def main():
    register_controllers()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


