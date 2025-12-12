from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        title = QLabel("Главная панель")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setObjectName("pageTitle")

        layout.addWidget(title)
