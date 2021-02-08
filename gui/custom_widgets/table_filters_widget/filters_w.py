from PySide6 import QtWidgets, QtCore

from gui.custom_widgets. \
     popup_field_widget. \
     popup_field_main import PopupFieldLabel


class FiltersWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lay_main_grid = QtWidgets.QGridLayout(self)
        self.lay_main_grid.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.lay_main_grid.setSpacing(0)

    def add_filter_field(self, items):
        filter_field = PopupFieldLabel(self, items)
        idx = self.lay_main_grid.columnCount()
        filter_field.field.textChanged.connect(lambda x, y=idx-1:
                                               self.start_filter_table(x, y))
        self.lay_main_grid.addWidget(filter_field, 0, idx)

    def start_filter_table(self, text, widget_idx):
        table_proxy_model = self.parent().table_view.proxy_model
        table_proxy_model.setFilterKeyColumn(widget_idx)
        table_proxy_model.setFilterWildcard(text)

    def show_widget(self, idx):
        w = self.lay_main_grid.itemAt(idx).widget()
        w.setVisible(True)

    def hide_widget(self, idx):
        w = self.lay_main_grid.itemAt(idx).widget()
        w.setVisible(False)

