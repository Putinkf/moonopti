from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from ui.pages.dashboard_page import DashboardPage
from ui.pages.optimization_page import OptimizationPage
from ui.pages.settings_page import SettingsPage
from ui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):
    def __init__(self, style_manager):
        super().__init__()
        self.style_manager = style_manager

        self.setWindowTitle("System Optimizer")
        self.resize(1100, 720)

        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        self.sidebar = Sidebar(on_change=self.switch_page, on_theme_switch=self.toggle_theme)
        main_layout.addWidget(self.sidebar)

        # Центр — страницы
        self.stacked = QStackedWidget()
        self.pages = {
            "dashboard": DashboardPage(),
            "optimization": OptimizationPage(),
            "settings": SettingsPage()
        }
        for p in self.pages.values():
            self.stacked.addWidget(p)

        main_layout.addWidget(self.stacked)

        self.setCentralWidget(main_widget)

    def switch_page(self, name):
        if name in self.pages:
            widget = self.pages[name]
            self.stacked.setCurrentWidget(widget)

    def toggle_theme(self):
        self.style_manager.toggle_theme()
