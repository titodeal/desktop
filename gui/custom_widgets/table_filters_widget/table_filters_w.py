from PySide6 import QtWidgets, QtCore
from .table_view import TableView
from .filters_w import FiltersWidget
from gui.utils import window_managment


class TableFilterScrollArea(QtWidgets.QScrollArea):
    def __init__(self, parent=None, objects=[], headers=[], filter_list=True):
        super().__init__(parent)
        self.table_filters = TableFiltersWidget(self, objects, headers, filter_list)
        self.table_view = self.table_filters.table_view
        self.append_rows = self.table_filters.append_rows
        self.insert_rows = self.table_filters.insert_rows
        self.setWidget(self.table_filters)

#         print(self.table_filters.sizeHint())


class TableFiltersWidget(QtWidgets.QWidget):
    """objects - list of some class objects;
       headers - list of some class objects attributes"""
    def __init__(self, parent=None, objects=[], headers=[], filter_list=True):
        super().__init__(parent)

        self.resize(200, 100)
        window_managment.adjust_by_screen(self)

        self.filter_list = filter_list

        # ---------  Layouts ------------------
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_vert.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.lay_main_vert.setSpacing(0)

        # ---------  Widgets ------------------
        self.table_view = TableView(self, objects, headers)
        self.filters_widget = FiltersWidget(self)
        self._add_filter_fields()

        # ---------  Setup Layouts ------------------
        self.lay_main_vert.addWidget(self.filters_widget)
        self.lay_main_vert.addWidget(self.table_view)

#         self.update_table_data(objects)
#         window_managment.set_mergins(self, self.lay_header_hori, 0.02, 0.1)
#         self.filters_widget.adjust_pudding_space()

    def _get_column_data(self, column_idx):
        return self.table_view.get_all_column_data(column_idx) if self.filter_list else []

    def _add_filter_fields(self):
        headers = self.table_view.model.headers
        for idx, header in enumerate(headers):
            items = self._get_column_data(idx)
            self.filters_widget.add_filter_field(items, header)

    def get_current_index(self):
        idx = self.table_view.selection_model.currentIndex()
        print(idx.data())

    def insert_rows(self, objects_data, row=0):
        self.table_view.model.insertRows(objects_data, row)

    def append_rows(self, objects_data):
        row_count = self.table_view.model.rowCount()
        self.table_view.model.insertRows(objects_data, row_count)

    def set_items_flags(self, flags):
        self.table_view.model.set_flags(flags)

    def set_items_checkable(self, _bool):
        self.table_view.model.set_checkable(_bool)

    def enable_filter_list(self, bool_):
        self.filter_list = bool_
        self._update_filter_list()

    def enable_hheaders_visible(self, _bool):
        self.table_view.hheader.setVisible(_bool)

    def enable_vheaders_visible(self, _bool):
        self.table_view.vheader.setVisible(_bool)

    def set_visible_hheaders(self, headers_list=[]):
        all_headers = self.table_view.model.headers
        for idx, header in enumerate(all_headers):
            if header in headers_list:
                self.table_view.hheader.showSection(idx)
                self.filters_widget.show_filter(header)
                self.table_view.header_menu.actions()[idx].setChecked(True)
            else:
                self.table_view.hheader.hideSection(idx)
                self.filters_widget.hide_filter(header)
                self.table_view.header_menu.actions()[idx].setChecked(False)

    def set_first_column_movable(self, bool_):
        self.table_view.hheader.setFirstSectionMovable(bool_)

    def update_table_data(self, objects):
        self.table_view.model.update_data(objects)
        self._update_filter_list()

    def _update_filter_list(self):
        all_headers = self.table_view.model.headers
        for idx, header in enumerate(all_headers):
            items = self._get_column_data(idx)
            self.filters_widget.update_popup_list(header, items)
