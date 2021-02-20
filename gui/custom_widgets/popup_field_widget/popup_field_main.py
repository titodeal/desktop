from PySide6 import QtWidgets, QtCore
from .popup_field import PopupField


class PopupFieldLabel(QtWidgets.QWidget):
    def __init__(self, parent=None, items=[], label = ""):

        super().__init__(parent)

        self.lay_main = QtWidgets.QVBoxLayout(self)
        self.lay_main.setContentsMargins(0, 5, 0, 0)

        self.name = label
        self.lb_label = QtWidgets.QLabel(self)
        self.lb_label.setText(self.name)

        self.field = PopupField(self, items)

        self.lay_main.addWidget(self.field)
        self.lb_label.raise_()

    def _set_label_pos(self):
        rect = self.field.geometry()

        field_width = rect.width()
        lb_width = self.lb_label.size().width()
        lb_height = self.lb_label.size().height()

        x_pos = (field_width - lb_width) / 2
        y_pos = rect.top() - lb_height / 2

        self.lb_label.move(x_pos, y_pos)

    def resizeEvent(self, event):
        self._set_label_pos()

    def set_label_text(self, text):
        self.lb_label.setText(text)

    def update_popup_list(self, items):
        self.field.update_list_data(items)
        self.field.size_list_done = False
