from PySide6 import QtWidgets, QtCore
from .table_view import TableView
from .filters_w import FiltersWidget
# from gui.custom_widgets.popup_field_widget.list_field import PopupField as FiltersWidget

from gui.utils import window_managment


class TableFiltersWidget(QtWidgets.QWidget):
    """objects - list of some class objects;
       headers - list of some class objects attributes"""
    def __init__(self, parent=None, objects=[], headers=[]):
        super().__init__(parent)

        self.resize(200, 100)
        window_managment.adjust_by_screen(self)

        # ---------  Layouts ------------------
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_vert.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.lay_main_vert.setSpacing(0)

        # ---------  Widgets ------------------
        self.table_view = TableView(self, objects, headers)
        self.filters_widget = FiltersWidget(self)
        self.add_filter_fields()

        # ---------  Setup Layouts ------------------
        self.lay_main_vert.addWidget(self.filters_widget)
        self.lay_main_vert.addWidget(self.table_view)

#         window_managment.set_mergins(self, self.lay_header_hori, 0.02, 0.1)

    def add_filter_fields(self):
        headers = self.table_view.model.headers
        for idx, header in enumerate(headers):
            column_data = self.table_view.get_all_column_data(idx)
            self.filters_widget.add_filter_field(column_data)

    def get_current_index(self):
        idx = self.table_view.selection_model.currentIndex()
        print(idx.data())

    def set_items_flags(self, flags):
        self.table_view.model.set_flags(flags)

    def set_items_checkable(self, _bool):
        self.table_view.model.set_checkable(_bool)

    def set_hheaders_visible(self, _bool):
        self.table_view.hheader_view.setVisible(_bool)

    def set_vheaders_visible(self, _bool):
        self.table_view.vheader_view.setVisible(_bool)
