from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from models.tabs_component_model import TabsComponentModel

from utils.decorators.state_subscribe_decorator import state_model_subscribe

from ui.components.thumbnail_listview_component.thumbnail_listview_component import ThumbnailListviewComponent

from ui.components.tabs_component.tabs_component_commands.change_primary_image_command import ChangePrimaryImageCommand

from config.constants import AppStateConstants

import os


@state_model_subscribe
class TabsComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = TabsComponentModel()

        self.layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

        self.setStyleSheet("border: 1px solid red;")

    def react_state_update(self, key, value):

        updated_tabs = self.compare_tab_images(value)
        self.model.tab_images_map = value

        for directory, images in updated_tabs.items():
            tab_name = os.path.basename(directory)

            if tab_name not in self.get_existing_tabs():
                self.add_tab(tab_name, images)
            else:
                self.update_tab_images(tab_name, images)

    def add_tab(self, name, images):
        tab = QWidget()
        tab_layout = QVBoxLayout()

        thumbnail_listview = ThumbnailListviewComponent(images)
        thumbnail_listview.list_item_clicked.connect(self.on_image_selected)
        tab_layout.addWidget(thumbnail_listview)
        tab.setLayout(tab_layout)

        self.tab_widget.addTab(tab, name)

    def update_tab_images(self, tab_name, images):
        tab_index = self.get_existing_tabs().index(tab_name)

        existing_tab = self.tab_widget.widget(tab_index)
        thumbnail_listview = existing_tab.layout().itemAt(0).widget()
        thumbnail_listview.update_listview(images)

    def compare_tab_images(self, value):
        updated_tabs = {}

        print(value)

        for directory, images in value.items():
            if directory in self.model.tab_images_map:
                existing_images = self.model.tab_images_map[directory]

                added_images = images - existing_images

                if added_images:
                    updated_tabs[directory] = added_images

            else:
                updated_tabs[directory] = images

        return updated_tabs

    def get_existing_tabs(self):
        return [self.tab_widget.tabText(i) for i in range(self.tab_widget.count())]

    def on_image_selected(self, image_path):
        print('IMAGE_PATH', image_path)
        return ChangePrimaryImageCommand(**{AppStateConstants.PRIMARY_IMAGE_PATH.value: image_path})


