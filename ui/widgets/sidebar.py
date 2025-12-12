from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt


class Sidebar(QWidget):
    def __init__(self, on_change, on_theme_switch):
        super().__init__()

        self.on_change = on_change
        self.on_theme_switch = on_theme_switch

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("System Optimizer")
        title.setObjectName("sidebarTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout.addWidget(title)

        # Кнопки
        btn_home = self._make_button("Главная", lambda: on_change("dashboard"))
        btn_opt = self._make_button("Оптимизация", lambda: on_change("optimization"))
        btn_set = self._make_button("Настройки", lambda: on_change("settings"))

        layout.addWidget(btn_home)
        layout.addWidget(btn_opt)
        layout.addWidget(btn_set)

        # Divider
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setObjectName("divider")
        layout.addWidget(divider)

        theme_btn = self._make_button("Сменить тему", on_theme_switch)
        layout.addWidget(theme_btn)

        layout.addStretch()

    def _make_button(self, text, func):
        btn = QPushButton(text)
        btn.setObjectName("sidebarButton")
        btn.clicked.connect(func)
        return btn
