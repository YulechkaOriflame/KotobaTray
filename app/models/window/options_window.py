from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from app.models.button.apply_settings_button import ApplySettingButton

LANGUAGES = ["ru", "en", "ja", "fr", "de", "es", "ar", "pl", "da", "sw", "zh", "ko", "it", "auto"]

class Options(QWidget):
    def __init__(self):
        super().__init__()
        self._source_lang = "ja"
        self._target_lang = "ru"
        self._show_sound_button = True
        self._build_layout()
        self.adjustSize()

    def get_src(self) -> str:
        return self._source_lang

    def get_tgt(self) -> str:
        return self._target_lang

    def _build_layout(self):
        self.layout = QVBoxLayout(self)
        source_widget, self.source_box = self._box_lang("Source language", self._source_lang)
        self.layout.addWidget(source_widget)

        target_widget, self.target_box = self._box_lang("Target language", self._target_lang)
        self.layout.addWidget(target_widget)

        self._add_apply_button()
        self.setLayout(self.layout)

    def _add_apply_button(self):
        self.apply_button = ApplySettingButton(self)
        self.layout.addWidget(self.apply_button)

    @staticmethod
    def _box_lang(name: str, language: str) -> tuple[QWidget, QComboBox]:
        wrapper, layout = Options._create_wrapper()
        label, box = Options._create_label_and_box(name, language)
        Options._add_widgets_to_layout(layout, [label, box])
        return wrapper, box

    @staticmethod
    def _create_wrapper() -> tuple[QWidget, QVBoxLayout]:
        wrapper = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        wrapper.setLayout(layout)
        return wrapper, layout

    @staticmethod
    def _create_label_and_box(name: str, language: str) -> tuple[QLabel, QComboBox]:
        label = QLabel(name)
        box = QComboBox()
        box.addItems(LANGUAGES)
        box.setCurrentText(language)
        return label, box

    @staticmethod
    def _add_widgets_to_layout(layout: QVBoxLayout, widgets: list):
        for w in widgets:
            layout.addWidget(w)
