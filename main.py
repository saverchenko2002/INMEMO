import sys
import logging
from PyQt6.QtWidgets import QApplication
import importlib

from core.initialize import register_controllers, initialize_services

from ui.main_window import MainWindow


import faulthandler


def main():
    logging.basicConfig(level=logging.INFO)
    initialize_services()
    register_controllers()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    import sys

    std_modules = ["os", "sys", "json", "re", "logging", "shutil", "datetime", "time", "threading", "random", "math",
                   "urllib"]

    for mod in std_modules:
        try:
            module = importlib.import_module(mod)
            print(f"{mod}: {module.__file__}")
        except Exception as e:
            print(f"Ошибка при импорте {mod}: {e}")
    print('//////////////////////////////////')

    print(sys.modules.keys())
    print('//////////////////////////////////')


    print(sys.path)
    print('//////////////////////////////////')
    print(sys.modules)

    faulthandler.enable()
    main()


