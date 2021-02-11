from PySide6 import QtWidgets, QtCore
from .table_view import TableView
from .filters_w import FiltersWidget
from gui.utils import window_managment


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
        self.add_filter_fields()

        # ---------  Setup Layouts ------------------
        self.lay_main_vert.addWidget(self.filters_widget)
        self.lay_main_vert.addWidget(self.table_view)

#         window_managment.set_mergins(self, self.lay_header_hori, 0.02, 0.1)

    def add_filter_fields(self):
        headers = self.table_view.model.headers
        for idx, header in enumerate(headers):
            items = self._get_filter_items(idx)
            self.filters_widget.add_filter_field(items, header)

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

    def set_visible_hheaders(self, headers_list=[]):
        all_headers = self.table_view.model.headers
        for idx, header in enumerate(all_headers):
            if header in headers_list:
                self.table_view.hheader_view.showSection(idx)
                self.filters_widget.show_filter(header)
                self.table_view.header_menu.actions()[idx].setChecked(True)
            else:
                self.table_view.hheader_view.hideSection(idx)
                self.filters_widget.hide_filter(header)
                self.table_view.header_menu.actions()[idx].setChecked(False)

    def update_table_data(self, objects):
        self.table_view.model.update_data(objects)
        self.update_filter_list()

    def _get_filter_items(self, column_idx):
        return self.table_view.get_all_column_data(column_idx) if self.filter_list else []

    def update_filter_list(self):
        all_headers = self.table_view.model.headers
        for idx, header in enumerate(all_headers):
            items = self._get_filter_items(idx)
            self.filters_widget.update_popup_list(header, items)

    def enable_filter_list(self, bool_):
        self.filter_list = bool_
        self.update_filter_list()

