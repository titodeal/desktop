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

    def add_filter_field(self, items, label):
        filter_field = PopupFieldLabel(self, items, label)
        self.lay_main_hor.addWidget(filter_field)
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
        widgets_count = self.lay_main_hor.count()
        for i in range(widgets_count):
            w = self.lay_main_hor.itemAt(i).widget()
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
        w1 = self.lay_main_hor.itemAt(from_idx).widget()
        self.lay_main_hor.removeWidget(w1)
        self.lay_main_hor.insertWidget(to_idx, w1)

        # ----------- Swap actions -----------
        header_menu = self.parent().table_view.header_menu
        action = header_menu.actions()[from_idx]
#         if from_idx > to_idx:
#             action_before = header_menu.actions()[to_idx]
#         elif len(header_menu.actions()) == to_idx + 1:
#             action_before = None
#         else:
#             action_before = header_menu.actions()[to_idx + 1]
#         header_menu.removeAction(action)
#         header_menu.insertAction(action_before, action)



