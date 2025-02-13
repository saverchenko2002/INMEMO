from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QApplication

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout


from menu.menu_bar import MenuBar
from core.command_publisher import CommandPublisher
from core.command_executor import CommandExecutor

from ui.components.directory_component import DirectoryComponent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(QApplication.primaryScreen().size().width()//2, QApplication.primaryScreen().size().height()//2)

        self.setWindowTitle("Image Processing App")
        self.setMenuBar(MenuBar(self))
        CommandPublisher.subscribe(self)

        self.top_area = None
        self.work_area = None
        self.bottom_area = None

        self.directory_component = None
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

        self.directory_component = DirectoryComponent()

        main_layout.addWidget(self.top_area, 1)
        main_layout.addWidget(self.work_area, 8)
        main_layout.addWidget(self.bottom_area, 1)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addWidget(self.directory_component)
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
         """)



    def outdated(self):
        layout = QVBoxLayout()  # container

        tools_panel = QHBoxLayout()
        main_panel = QHBoxLayout()
        status_panel = QHBoxLayout()

        tools_widget = QWidget()
        tools_widget.setLayout(tools_panel)

        tools_widget.setStyleSheet("border: 1px solid green;")

        main_widget = QWidget()
        main_widget.setLayout(main_panel)
        main_widget.setStyleSheet("border: 1px solid red;")

        status_widget = QWidget()
        status_widget.setLayout(status_panel)
        status_widget.setStyleSheet("border: 1px solid black;")

        label1 = QLabel("Добро пожаловать в приложение!1")
        label2 = QLabel("Добро пожаловать в приложение!2Добро пожаловать в приложение!2Добро пожаловать в приложение!2")

        main_panel.addWidget(PwdComponent(PwdModel('putin')))
        main_panel.addWidget(label1)
        main_panel.addWidget(label2)

        status_panel.addWidget(PwdComponent(PwdModel('putin')))

        layout.addWidget(tools_widget)
        layout.addWidget(main_widget)
        layout.addWidget(status_widget)

        layout.setStretch(0, 1)
        layout.setStretch(1, 8)
        layout.setStretch(2, 1)

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


