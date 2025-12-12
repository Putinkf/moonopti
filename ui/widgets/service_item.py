from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt

from ui.widgets.toggle_switch import ToggleSwitch


class ServiceItem(QWidget):
    def __init__(self, title, description, status=True):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(12)

        # Title + description stack
        text_area = QWidget()
        text_layout = QHBoxLayout(text_area)
        text_layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(f"<b>{title}</b> — {description}")
        label.setWordWrap(True)
        text_layout.addWidget(label)

        # Toggle
        self.toggle = ToggleSwitch(checked=status)

        # Button (e.g. details)
        btn = QPushButton("Подробнее")
        btn.setObjectName("serviceDetailsButton")

        layout.addWidget(text_area)
        layout.addWidget(self.toggle)
        layout.addWidget(btn)
        layout.addStretch()
