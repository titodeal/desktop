from PySide6 import QtWidgets, QtCore, QtGui

from .popup_list_view import PopupListView


class PopupField(QtWidgets.QLineEdit):
    def __init__(self, parent=None, items=[]):
        super().__init__(parent)

#         self.setFrame(False)

        self.complete = False 
        self.can_popup = True
        self.list_view = PopupListView(self, items)
        self.list_view.setWindowFlags(QtCore.Qt.Tool
                                       | QtCore.Qt.FramelessWindowHint)

        self.list_view.clicked.connect(self.click_select_item)
        self.textChanged.connect(self.set_filter_proxy)

        self.size_by_items = 5

    def set_filter_proxy(self, text):
        if not self.list_view.isVisible():
            self.list_view.show()
        self.list_view.proxy_model.setFilterWildcard(text)
        self.list_view.set_current_index(0)

    def click_select_item(self, index):
        self.setText(index.data())
        self.set_current_item_value()

    def set_current_item_value(self):
        if self.text():
            curr_idx = self.list_view.get_current_index()
            self.setText(curr_idx.data())
        self.list_view.close()
        self.can_popup = False

    def focusInEvent(self, event):
#         self.complete = False
        self.size_pos_list_wdg()
        self.list_view.show()
        QtWidgets.QLineEdit.focusInEvent(self, event)
# 
    def focusOutEvent(self, event):
#         if self.list_view.Visible():
        if not self.list_view.isActiveWindow():
            self.list_view.close()
#             self.complete = True

        QtWidgets.QLineEdit.focusOutEvent(self, event)

    def event(self, event):
        if isinstance(event, QtGui.QFocusEvent):
#         if event.type() == QtCore.QEvent.FocusIn:
            if event.gotFocus() and self.can_popup:
                pass
#                 self.activateWindow()
#                 self.size_pos_list_wdg()
#                 self.list_view.show()
            if event.lostFocus():
                pass
#                 if not self.list_view.isActiveWindow():
#                     self.list_view.close()
#                     self.can_popup = True

        if isinstance(event, QtCore.QEvent):
            if event.type() == QtCore.QEvent.KeyPress:
                if (event.key() == QtCore.Qt.Key_Return) or \
                   (event.key() == QtCore.Qt.Key_Enter):

                    self.set_current_item_value()

                if (event.key() == QtCore.Qt.Key_Down):
                    self.list_view.activateWindow()
                    self.list_view.setFocus()

        return QtWidgets.QWidget.event(self, event)

    def resizeEvent(self, size_event):
        if self.list_view.isVisible():
            self.size_pos_list_wdg()

    def size_pos_list_wdg(self):
        width = self.size().width()

        height_item = self.list_view.size_item().height()
        row_count = self.list_view.row_count()
        height = height_item * (row_count
                                if row_count < self.size_by_items
                                else self.size_by_items)

        x = self.mapToGlobal(QtCore.QPoint(0, 0)).x()
#         y = self.mapToGlobal(QtCore.QPoint(0, 0)).y() - height
        y = self.mapToGlobal(QtCore.QPoint(0, 0)).y() + self.height()
        self.list_view.setGeometry(x, y, width, height)

