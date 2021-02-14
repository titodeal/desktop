from PySide6 import QtWidgets, QtCore

from gui.custom_widgets. \
     popup_field_widget. \
     popup_field_main import PopupFieldLabel


class FiltersWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lay_main_hor = QtWidgets.QHBoxLayout(self)
        self.lay_main_hor.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.lay_main_hor.setSpacing(0)

        self.lay_filters_hor = QtWidgets.QHBoxLayout()
        self.lay_filters_hor.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        self.lay_filters_hor.setSpacing(0)

        self.lay_main_hor.addLayout(self.lay_filters_hor)
        self.lay_main_hor.insertSpacing(0, 0)
        self.lay_main_hor.addSpacing(0)

    def adjust_front_space(self, front_space):
        self.lay_main_hor.itemAt(0).changeSize(front_space, 0)
        self.lay_main_hor.invalidate()

    def adjust_last_space(self, last_space):
        count = self.lay_main_hor.count()
        self.lay_main_hor.itemAt(count-1).changeSize(last_space, 0)
        self.lay_main_hor.invalidate()

    def add_filter_field(self, items, label):
        filter_field = PopupFieldLabel(self, items, label)
        self.lay_filters_hor.addWidget(filter_field)
        filter_field.field.textChanged.connect(lambda x, y=label:
                                               self.start_filter_table(x, y))

    def start_filter_table(self, text, label):
        header_idx = self.parent().table_view.model.headers.index(label)
        table_proxy_model = self.parent().table_view.proxy_model
        table_proxy_model.setFilterKeyColumn(header_idx)
        table_proxy_model.setFilterWildcard(text)

    def update_popup_list(self, name_widget, items):
        w = self.get_filter_by_name(name_widget)
        w.update_popup_list(items)

    def get_filter_by_name(self, name):
        widgets_count = self.lay_filters_hor.count()
        for i in range(widgets_count):
            w = self.lay_filters_hor.itemAt(i).widget()
            if w is None:
                continue
            if name == w.name:
                return w

    def show_filter(self, name):
        w = self.get_filter_by_name(name)
        w.setVisible(True)

    def hide_filter(self, name):
        w = self.get_filter_by_name(name)
        w.setVisible(False)

    def swap_filters(self, from_idx, to_idx):
        # ----------- Swap widgets -----------
        w1 = self.lay_filters_hor.itemAt(from_idx).widget()
        self.lay_filters_hor.removeWidget(w1)
        self.lay_filters_hor.insertWidget(to_idx, w1)
        # ----------- Swap actions -----------
        header_menu = self.parent().table_view.header_menu
        action = header_menu.actions()[from_idx]
