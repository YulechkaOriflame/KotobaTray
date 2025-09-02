from app.models.window.base_window import BaseWindow
from app.models.options.windows_action import TrayAction

class WindowsManager:
    def __init__(self, menu, options):
        self.menu = menu
        self._windows: dict[str, tuple[BaseWindow, TrayAction]] = {}
        options.apply_button.applied.connect(self.hide_all)

    def create_windows(self, windows: dict[str, BaseWindow]):
        for name, win in windows.items():
            action = TrayAction(win, name, self.menu)
            self.menu.addAction(action)
            self._windows[name] = (win, action)

    def hide_all(self):
        for win, action in self._windows.values():
            win.hide()
            action.setChecked(False)