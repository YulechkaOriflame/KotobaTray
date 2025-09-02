from PySide6.QtGui import QAction

class TrayAction(QAction):
    def __init__(self, win, name, parent):
        super().__init__(name, parent, checkable=True)
        self.triggered.connect(lambda checked: win.setVisible(checked))