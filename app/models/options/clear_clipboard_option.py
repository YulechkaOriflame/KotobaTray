from PySide6.QtGui import QAction
from PySide6.QtWidgets import QSystemTrayIcon

from app.manager.clipboard_watcher import ClipboardWatcher

class ClearClipboardOption(QAction):
    def __init__(self, watcher: ClipboardWatcher, parent: QSystemTrayIcon):
        super().__init__("Clear clipboard", parent=parent)
        self._watcher = watcher
        self._parent = parent
        self.triggered.connect(self._on_toggled)

    def _on_toggled(self):
        self._watcher.clear()
