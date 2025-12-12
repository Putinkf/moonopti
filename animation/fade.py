from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6.QtWidgets import QWidget


class FadeAnimation:
    def __init__(self):
        self.anim = None

    def fade_in(self, widget: QWidget, duration=220):
        self.anim = QPropertyAnimation(widget, b"windowOpacity")
        self.anim.setDuration(duration)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        widget.show()
        self.anim.start()

    def fade_out(self, widget: QWidget, duration=220):
        self.anim = QPropertyAnimation(widget, b"windowOpacity")
        self.anim.setDuration(duration)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()
