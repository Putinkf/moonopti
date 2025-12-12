import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from themes.style_manager import StyleManager


def main():
    app = QApplication(sys.argv)

    # Подключаем менеджер стилей
    style = StyleManager()
    style.apply_light_theme(app)

    window = MainWindow(style)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
