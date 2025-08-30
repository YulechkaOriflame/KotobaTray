from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from app.models.options.clear_clipboard_option import ClearClipboardOption
from app.models.options.options_option import OptionsOption
from app.models.options.pause_option import PauseOption
from app.models.options.quit_option import QuitOption
from app.models.window.detailed_translate_from_jp import DetailedTranslateFromJp
from app.models.window.options_window import Options
from app.models.window.simple_translate_window import SimpleTranslate
from app.models.window.sticker_window import StickerWindow
from app.models.window.translate_to_window import TranslateToWindow
from app.manager.clipboard_watcher import ClipboardWatcher
from app.utils.loader import get_file
from app.manager.windows_manager import WindowsManager

class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.menu = QMenu()
        self._configure_icon()
        self.options = Options()
        self.clipboard_watcher = ClipboardWatcher()
        self.windows = WindowsManager(self.menu, self.options)
        self._configure_menu()

    def _configure_icon(self):
        self.setIcon(QIcon(get_file("tray-icon.png")))
        self.setToolTip("Kotoba")

    def _configure_menu(self):
        self.menu.addAction(OptionsOption(self.options, self))
        self.menu.addAction(ClearClipboardOption(self.clipboard_watcher, self))
        self.menu.addAction(PauseOption(self.clipboard_watcher, self))
        self.menu.addSeparator()
        self.windows.create_windows({
            "Sticker": StickerWindow(),
            "Detailed translate from JP": DetailedTranslateFromJp(self.options, self.clipboard_watcher),
            "Simple translate": SimpleTranslate(self.options, self.clipboard_watcher),
            "Translate to": TranslateToWindow(self.options),
        })
        self.menu.addSeparator()
        self.menu.addAction(QuitOption(self))
        self.setContextMenu(self.menu)