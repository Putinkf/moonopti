from PyQt6.QtCore import QFile, QTextStream


class StyleManager:
    def __init__(self):
        self.dark_mode = False

    def apply_light_theme(self, app):
        self._apply(app, "themes/light.qss")
        self.dark_mode = False

    def apply_dark_theme(self, app):
        self._apply(app, "themes/dark.qss")
        self.dark_mode = True

    def toggle_theme(self):
        from PyQt6.QtWidgets import QApplication
        app = QApplication.instance()
        if self.dark_mode:
            self.apply_light_theme(app)
        else:
            self.apply_dark_theme(app)

    def _apply(self, app, path):
        file = QFile(path)
        file.open(QFile.OpenModeFlag.ReadOnly)
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())
        file.close()
