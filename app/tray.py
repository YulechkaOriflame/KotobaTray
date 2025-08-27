from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon

from app.models.window.translate_to_window import TranslateToWindow
from app.models.window.sticker_window import StickerWindow
from app.models.window.translate_from_window import TranslationWindow
from app.utils.loader import get_tray_icon

class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self._configure_icon()
        self._configure_menu()

    def _configure_icon(self):
        icon = QIcon(get_tray_icon())
        self.setIcon(icon)

    def _configure_menu(self):
        self.menu = QMenu()
        self._create_windows({
            "Sticker": StickerWindow,
            "Translate from": TranslationWindow,
            "Translate to": TranslateToWindow,
        })
        self.menu.addSeparator()
        self._quit_option()
        self.setContextMenu(self.menu)

    def _create_windows(self, windows: dict):
        for name, cls in windows.items():
            win = cls()
            action = QAction(name, self)
            action.setCheckable(True)

            def toggle_window(checked, w=win):
                if checked:
                    w.show()
                else:
                    w.hide()

            action.triggered.connect(toggle_window)
            self.menu.addAction(action)

    def _quit_option(self):
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(QApplication.instance().quit)
        self.menu.addAction(exit_action)
