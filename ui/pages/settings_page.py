from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        title = QLabel("Настройки приложения")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setObjectName("pageTitle")

        layout.addWidget(title)
