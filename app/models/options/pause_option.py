from PySide6.QtGui import QAction
from PySide6.QtWidgets import QSystemTrayIcon

from app.manager.clipboard_watcher import ClipboardWatcher

class PauseOption(QAction):
    def __init__(self, watcher: ClipboardWatcher, parent: QSystemTrayIcon):
        super().__init__("Pause clipboard reading", parent=parent, checkable=True)
        self._watcher = watcher
        self._parent = parent
        self.toggled.connect(self._on_toggled)

    def _on_toggled(self, checked: bool):
        if checked:
            self._watcher.pause()
            self._parent.setToolTip("Kotoba (paused)")
        else:
            self._watcher.resume()
            self._parent.setToolTip("Kotoba")
