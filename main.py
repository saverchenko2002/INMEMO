import sys
import logging
from PyQt6.QtWidgets import QApplication

from core.initialize import register_controllers, initialize_services

from ui.main_window import MainWindow


def main():
    logging.basicConfig(level=logging.INFO)
    initialize_services()
    register_controllers()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


