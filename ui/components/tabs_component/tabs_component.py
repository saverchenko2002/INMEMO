from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QMessageBox

from models.tabs_component_model import TabsComponentModel

from utils.decorators.state_subscribe_decorator import state_model_subscribe

from ui.components.thumbnail_listview_component.thumbnail_listview_component import ThumbnailListviewComponent

from ui.components.tabs_component.tabs_component_commands.change_primary_image_command import ChangePrimaryImageCommand
from ui.components.tabs_component.tabs_component_commands.move_image_command import MoveImageCommand
from ui.components.tabs_component.tabs_component_commands.remove_tab_command import RemoveTabCommand
from ui.components.tabs_component.tabs_component_commands.change_tab_command import ChangeTabCommand

from ui.config.constants import FileSystemControlFlags
from ui.config.constants import DragDropConstants, MoveToTabConstants, RemoveTabConstants, ChangeTabConstants
from config.constants import AppStateConstants
import os
import json
import logging

@state_model_subscribe
class TabsComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.model = TabsComponentModel()

        self.layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self._close_tab)
        self.tab_widget.currentChanged.connect(self._on_tab_changed)
        self.setAcceptDrops(True)

        self.setStyleSheet("border: 1px solid red;")

    def react_state_update(self, key, value):

        if key == AppStateConstants.PRIMARY_TAB.value:
            self.model.primary_tab = value
            if value:
                self.set_active_tab_by_name(value)

        elif key == AppStateConstants.TAB_IMAGES_MAP.value:
            print('мы реактим на смену карты в таб компоненте, но карта', value)
            self.update_tab_images(value)
            self.model.tab_images_map = value

    def _close_tab(self, index):

        tab_name = self.tab_widget.tabText(index)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Подтверждение удаления")
        msg_box.setText(f"Вы уверены, что хотите удалить '{tab_name}'?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        response = msg_box.exec()

        if response == QMessageBox.StandardButton.Yes:
            self.tab_widget.currentChanged.disconnect(self._on_tab_changed)
            widget = self.tab_widget.widget(index)
            self.tab_widget.removeTab(index)
            if widget:
                widget.deleteLater()
            self.tab_widget.currentChanged.connect(self._on_tab_changed)

            return RemoveTabCommand(**{RemoveTabConstants.REMOVE_TAB_NAME.value: tab_name})

    def _on_tab_changed(self, index):
        tab_name = self.tab_widget.tabText(index)
        return ChangeTabCommand(**{ChangeTabConstants.CHANGE_TAB_NAME.value: tab_name})

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        tab_bar = self.tab_widget.tabBar()
        tab_index = tab_bar.tabAt(event.position().toPoint())

        if tab_index != -1:
            self.tab_widget.setCurrentIndex(tab_index)
        event.accept()

    def dropEvent(self, event):

        index = self.tab_widget.currentIndex()
        active_tab_name = self.tab_widget.tabText(index)
        if event.mimeData().hasText():
            data = json.loads(event.mimeData().text())
            image_path = data[DragDropConstants.IMAGE_PATH.value]

            source_dir_name = data[DragDropConstants.TAB_DIRECTORY.value]
            if os.path.basename(source_dir_name) == active_tab_name:
                event.ignore()
            elif os.path.basename(source_dir_name) != active_tab_name:
                MoveImageCommand(
                    **{MoveToTabConstants.SOURCE_IMAGE_PATH.value: image_path,
                       MoveToTabConstants.TARGET_FOLDER_NAME.value: active_tab_name})

    def add_tab(self, name, images):
        tab = QWidget()
        tab_layout = QVBoxLayout()

        thumbnail_listview = ThumbnailListviewComponent(images)
        thumbnail_listview.list_item_clicked.connect(self.on_image_selected)
        tab_layout.addWidget(thumbnail_listview)
        tab.setLayout(tab_layout)

        self.tab_widget.addTab(tab, name)

    def update_tab_images(self, value):

        for directory, images in value.items():
            tab_name = os.path.basename(directory)
            if directory in self.model.tab_images_map:
                added_images = [
                    added_image for added_image in images if added_image.filesystem_flag == FileSystemControlFlags.ADD_F
                ]
                removed_images = [
                    removed_image for removed_image in images if removed_image.filesystem_flag == FileSystemControlFlags.REMOVE_F
                ]
                renamed_images = [
                    renamed_image for renamed_image in images if renamed_image.filesystem_flag == FileSystemControlFlags.RENAME_F
                ]

                if added_images or removed_images or renamed_images:
                    tab_index = self.get_existing_tabs().index(tab_name)
                    existing_tab_widget = self.tab_widget.widget(tab_index)
                    thumbnail_listview = existing_tab_widget.layout().itemAt(0).widget()

                    if added_images:
                        for added_image in added_images:
                            print(added_image.filesystem_flag)
                            added_image.filesystem_flag = FileSystemControlFlags.NONE_F
                            thumbnail_listview.add_tile(added_image)
                    elif removed_images:
                        for removed_image in removed_images:
                            thumbnail_listview.remove_tile(removed_image)
                    elif renamed_images:
                        for renamed_image in renamed_images:
                            thumbnail_listview.rename_tile(renamed_image)
                        print('не ебу обновлён я или нет', self.model.tab_images_map)
            else:
                self.add_tab(tab_name, images)

        # print('value')
        # print(value)
        # print('self')
        # print(self.model.tab_images_map)
        # for directory, images in value.items():
        #     tab_name = os.path.basename(directory)
        #     if directory in self.model.tab_images_map:
        #         existing_images = self.model.tab_images_map[directory]
        #         added_images = [
        #             image for image in images
        #             if not any(existing_image.current_image_path == image.current_image_path for existing_image in
        #                        existing_images)
        #         ]
        #
        #         removed_images = [
        #             image for image in existing_images
        #             if
        #             not any(existing_image.current_image_path == image.current_image_path for existing_image in images)
        #         ]
        #
        #         renamed_images = [
        #             image for image in images
        #             if not any(existing_image.original_image_path == image.original_image_path for existing_image in
        #                        existing_images)
        #         ]
        #
        #         if added_images or removed_images or renamed_images:
        #             tab_index = self.get_existing_tabs().index(tab_name)
        #             existing_tab = self.tab_widget.widget(tab_index)
        #             thumbnail_listview = existing_tab.layout().itemAt(0).widget()
        #
        #             if added_images:
        #                 thumbnail_listview.update_listview(added_images)
        #             elif removed_images:
        #                 for image in removed_images:
        #                     thumbnail_listview.remove_tile(image)
        #             elif renamed_images:
        #                 for image in renamed_images:
        #                     thumbnail_listview.rename_tile(image)
        #
        #                     image.original_image_path = image.current_image_path
        #
        #                     for idx, existing_image in enumerate(self.model.tab_images_map[directory]):
        #                         if existing_image.original_image_path == image.original_image_path:
        #                             self.model.tab_images_map[directory][idx] = image
        #                             break
        #
        #     else:
        #         self.add_tab(tab_name, images)
        #     logging.info(value)

    def get_existing_tabs(self):
        return [self.tab_widget.tabText(i) for i in range(self.tab_widget.count())]

    def on_image_selected(self, image_path):
        return ChangePrimaryImageCommand(**{AppStateConstants.PRIMARY_IMAGE_PATH.value: image_path})

    def set_active_tab_by_name(self, name):
        name = os.path.basename(name)
        for i in range(self.tab_widget.count()):
            if self.tab_widget.tabText(i) == name:
                self.tab_widget.setCurrentIndex(i)
                break
