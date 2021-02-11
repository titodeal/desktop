from PySide6 import QtWidgets, QtCore, QtGui

from .popup_list_view import PopupListView


class PopupField(QtWidgets.QLineEdit):
    def __init__(self, parent=None, items=[]):
        super().__init__(parent)

        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.list_view = PopupListView(self, items)
        self.list_view.setWindowFlags(QtCore.Qt.Tool
                                       | QtCore.Qt.FramelessWindowHint)

        self.list_view.clicked.connect(self._set_clicked_value)
        self.textChanged.connect(self._set_filter_proxy)

        self.size_list_done = False
        self.size_by_items = 5

    def _set_filter_proxy(self, text):
        if not self.list_view.isVisible():
            self.list_view.show()
        self.list_view.proxy_model.setFilterWildcard(text)

    def _set_clicked_value(self, index):
        self.set_selected_value()

    def set_selected_value(self, can_empty=False):
        if self.list_view.proxy_model.rowCount() <= 0:
            value = self.text()
        elif not self.text() and can_empty:
            value = ""
        else:
            value = self.list_view.get_selected_index().data()

        self.setText(value)
        self.setFocus()
        self.list_view.close()

    def update_list_data(self, items):
        self.list_view.model.update_data(items)

    # --------------- Events --------------
    def focusInEvent(self, event):
        if not self.size_list_done:
            self.size_pos_list()
            self.size_list_done = True
        if not event.reason() == QtCore.Qt.ActiveWindowFocusReason:
            self.list_view.show()
        return QtWidgets.QLineEdit.focusInEvent(self, event)
# 
    def focusOutEvent(self, event):
        if not (event.reason() == QtCore.Qt.TabFocusReason
           or event.reason() == QtCore.Qt.ActiveWindowFocusReason):
            self.list_view.close()
        return QtWidgets.QLineEdit.focusOutEvent(self, event)

    def focusNextPrevChild(self, bool_):
        return False

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Return) or \
           (event.key() == QtCore.Qt.Key_Enter):
            self.set_selected_value(True)

        if (event.key() == QtCore.Qt.Key_Down) or \
           (event.key() == QtCore.Qt.Key_Tab):
            if not self.list_view.isVisible():
                self.list_view.show()
            self.list_view.activateWindow()
            self.list_view.setFocus()

        if event.key() == QtCore.Qt.Key_Escape:
            self.list_view.close()
        return QtWidgets.QLineEdit.keyPressEvent(self, event)

    def resizeEvent(self, size_event):
        if self.list_view.isVisible():
            self.size_pos_list()
        else:
            self.size_list_done = False

    def size_pos_list(self):
        width = self.size().width()

        height_item = self.list_view.size_item().height()
        row_count = self.list_view.row_count()
        height = height_item * (row_count
                                if row_count < self.size_by_items
                                else self.size_by_items)

        x = self.mapToGlobal(QtCore.QPoint(0, 0)).x()
        y = self.mapToGlobal(QtCore.QPoint(0, 0)).y() + self.height()
        self.list_view.setGeometry(x, y, width, height)

