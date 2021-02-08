from PySide6 import QtWidgets, QtCore

# from .popup_list_view import PopupListView
from gui.custom_widgets.popup_field_widget.popup_field import PopupField


class FiltersWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lay_main_grid = QtWidgets.QGridLayout(self)
        self.lay_main_grid.setContentsMargins(QtCore.QMargins(1, 0, 1, 5))

    def add_filter_field(self, items):
        filter_field = PopupField(self, items)

        idx = self.lay_main_grid.columnCount()
        filter_field.textChanged.connect(lambda x, y=idx-1:
                                         self.start_filter_table(x, y))

        self.lay_main_grid.addWidget(filter_field, 0, idx)

    def start_filter_table(self, text, widget_idx):
        table_proxy_model = self.parent().projects_table.proxy_model
        table_proxy_model.setFilterKeyColumn(widget_idx)
        table_proxy_model.setFilterWildcard(text)

    def show_widget(self, idx):
        w = self.lay_main_grid.itemAt(idx).widget()
        w.setVisible(True)

    def hide_widget(self, idx):
        w = self.lay_main_grid.itemAt(idx).widget()
        w.setVisible(False)


# class PopupField(QtWidgets.QLineEdit):
#     def __init__(self, parent=None, items=[]):
#         super().__init__(parent)
# 
#         self.can_popup = True
#         self.list_items = PopupListView(self, items)
#         self.list_items.setWindowFlags(QtCore.Qt.Tool
#                                        | QtCore.Qt.FramelessWindowHint)
# 
#         self.list_items.clicked.connect(self.click_select_item)
#         self.textChanged.connect(self.set_filter_items)
# 
#     def set_filter_items(self, text):
#         if not self.list_items.isVisible():
#             self.list_items.show()
#         self.list_items.proxy_model.setFilterWildcard(text)
# #         self.list_items.proxy_model.setFilterRegularExpression(text)
#         self.list_items.set_current_index(0)
# 
#     def click_select_item(self, index):
#         self.setText(index.data())
#         self.set_current_item_value()
# 
#     def set_current_item_value(self):
#         if not self.text():
#             pass
#         else:
#             curr_idx = self.list_items.get_current_index()
#             self.setText(curr_idx.data())
#         self.list_items.close()
#         self.can_popup = False
# 
#     def event(self, event):
#         if isinstance(event, QtGui.QFocusEvent):
#             if event.gotFocus() and self.can_popup:
#                 self.size_pos_list_wdg()
#                 self.list_items.show()
#             if event.lostFocus():
#                 if not self.list_items.isActiveWindow():
#                     self.list_items.close()
#                     self.can_popup = True
# 
#         if isinstance(event, QtCore.QEvent):
#             if event.type() == QtCore.QEvent.KeyPress:
#                 if (event.key() == QtCore.Qt.Key_Return) or \
#                    (event.key() == QtCore.Qt.Key_Enter):
# 
#                     self.set_current_item_value()
# 
#         return QtWidgets.QWidget.event(self, event)
# 
#     def resizeEvent(self, size_event):
#         if self.list_items.isVisible():
#             self.size_pos_list_wdg()
# 
#     def size_pos_list_wdg(self):
#         width = self.size().width()
#         height = 100
#         x = self.mapToGlobal(QtCore.QPoint(0, 0)).x()
#         y = self.mapToGlobal(QtCore.QPoint(0, 0)).y() - height
#         self.list_items.setGeometry(x, y, width, height)
# 
