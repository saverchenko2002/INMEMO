from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from config.constants import AppNameConstants

from menu.menu_bar import MenuBar
from core.command_publisher import CommandPublisher
from core.command_executor import CommandExecutor

from ui.components.directory_component.directory_component import DirectoryComponent
from ui.components.app_status_component.app_status_component import AppStatusComponent
from ui.components.tabs_component.tabs_component import TabsComponent
from ui.components.image_container_component.image_container_component import ImageContainerComponent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(QApplication.primaryScreen().size().width()//2, QApplication.primaryScreen().size().height()//2)

        self.setWindowTitle(AppNameConstants.APPLICATION_TITLE.value)
        self.setMenuBar(MenuBar(self))
        CommandPublisher.subscribe(self)

        self.top_area = None
        self.work_area = None
        self.bottom_area = None

        self.image_area = None
        self.tabs_area = None

        self.directory_component = None
        self.app_status_component = None
        self.tabs_component = None
        self.image_container_component = None

        self.work_area_layout = None
        self.bottom_layout = None

        self.init_ui()

    def init_ui(self):

        central_widget = QWidget()
        main_layout = QVBoxLayout()

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.top_area = QWidget()
        self.top_area.setObjectName("TopArea")
        self.work_area = QWidget()
        self.work_area.setObjectName("WorkArea")
        self.bottom_area = QWidget()
        self.bottom_area.setObjectName("BottomArea")

        self.image_area = QWidget()
        self.image_area.setObjectName("ImageArea")
        self.tabs_area = QWidget()
        self.tabs_area.setObjectName("TabsArea")

        self.directory_component = DirectoryComponent()
        self.app_status_component = AppStatusComponent()
        self.tabs_component = TabsComponent()
        self.image_container_component = ImageContainerComponent()

        main_layout.addWidget(self.top_area, 1)
        main_layout.addWidget(self.work_area, 8)
        main_layout.addWidget(self.bottom_area, 1)

        image_container_layout = QVBoxLayout()
        image_container_layout.addWidget(self.image_container_component)
        self.image_area.setLayout(image_container_layout)

        tabs_layout = QVBoxLayout()
        tabs_layout.addWidget(self.tabs_component)
        self.tabs_area.setLayout(tabs_layout)

        self.work_area_layout = QHBoxLayout()
        self.work_area_layout.addWidget(self.image_area, 7)
        self.work_area_layout.addWidget(self.tabs_area, 3)
        self.work_area.setLayout(self.work_area_layout)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addWidget(self.app_status_component, 2)
        self.bottom_layout.addWidget(self.directory_component, 8)
        self.bottom_area.setLayout(self.bottom_layout)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
             #TopArea {
                 border: 1px solid green
             }
             #WorkArea {
                 border: 1px solid red
             }
             #BottomArea {
                 border: 1px solid black
             }
             #ImageArea {
                 border: 1px solid blue
             }
             #TabsArea {
                 border: 1px solid black
             }
         """)

    def close_event(self, event):
        CommandPublisher.unsubscribe(self)

    @staticmethod
    def on_command_received(command):
        CommandExecutor.execute(command)


