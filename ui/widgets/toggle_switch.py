from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QRectF, QPropertyAnimation, pyqtProperty
from PyQt6.QtGui import QPainter, QColor


class ToggleSwitch(QWidget):
    def __init__(self, checked=False, parent=None):
        super().__init__(parent)
        self._checked = checked
        self._handle_pos = 1 if checked else 0

        self.setFixedSize(50, 26)

        self.anim = QPropertyAnimation(self, b"handlePos")
        self.anim.setDuration(160)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._checked = not self._checked
            self.anim.setStartValue(self._handle_pos)
            self.anim.setEndValue(1 if self._checked else 0)
            self.anim.start()
            self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Background
        bg_color = QColor("#4caf50") if self._checked else QColor("#999999")
        p.setBrush(bg_color)
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(0, 0, self.width(), self.height(), 13, 13)

        # Handle
        x = 2 + (self.width() - 26 - 4) * self._handle_pos
        p.setBrush(QColor("#ffffff"))
        p.drawEllipse(QRectF(x, 2, 22, 22))

    @pyqtProperty(float)
    def handlePos(self):
        return self._handle_pos

    @handlePos.setter
    def handlePos(self, pos):
        self._handle_pos = pos
        self.update()

    def isChecked(self):
        return self._checked
