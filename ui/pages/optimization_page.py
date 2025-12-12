from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class OptimizationPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        title = QLabel("Оптимизация системы")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setObjectName("pageTitle")

        layout.addWidget(title)
