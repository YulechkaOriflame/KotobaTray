from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton

class ApplySettingButton(QPushButton):
    applied = Signal()

    # noinspection PyUnresolvedReferences
    def __init__(self, options_widget: "Options"):
        super().__init__("Apply")
        self._options_widget = options_widget
        self.clicked.connect(self._apply_changes)

    def _apply_changes(self):
        new_source = self._options_widget.source_box.currentText()
        new_target = self._options_widget.target_box.currentText()

        self._options_widget._source_lang = new_source
        self._options_widget._target_lang = new_target
        self._options_widget.hide()

        self.applied.emit()
