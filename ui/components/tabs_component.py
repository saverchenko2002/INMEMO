from core.app_state_service import AppStateService

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QListView

from models.tabs_component_model import TabsComponentModel

import re

class TabsComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = TabsComponentModel()

        self.layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

        self.setStyleSheet("border: 1px solid red;")

        for field in vars(self.model).keys():
            print(f'подписались ежжи по полю{field}')
            print(self)
            AppStateService().subscribe(field, self)

    def react_state_update(self, key, value):
        print('я внутри tabs component бро')
        print(key)
        print(value)
        if value:
            first_item = next(iter(value))
            tab_name = re.search(r'[^\\/]+$', first_item).group()
            print(tab_name)
            self.add_tab(tab_name)

        # print('DirectoryComponentModel сначала я получаю доступ')
        # print('DirectoryComponentModel сначала я получаю доступ')
        # self.model[key] = value
        # self.directory_label.setText(self.model[key])

    def add_tab(self, name):
        tab = QWidget()
        tab_layout = QVBoxLayout()

        list_view = QListView()
        tab_layout.addWidget(list_view)

        tab.setLayout(tab_layout)
        self.tab_widget.addTab(tab, name)
