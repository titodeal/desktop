from PySide6 import QtWidgets, QtCore, QtGui

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

        self.is_showed = False

    def adjust_front_space(self, front_space):
        self.lay_main_hor.itemAt(0).changeSize(front_space, 0)
        self.lay_main_hor.invalidate()

    def adjust_last_space(self, last_space):
        count = self.lay_main_hor.count()
        self.lay_main_hor.itemAt(count-1).changeSize(last_space, 0)
        self.lay_main_hor.invalidate()

    def _match_with_columns(self):
        header_view = self.parent().table_view.hheader
        headers = self.parent().table_view.model.headers
        for idx, header in enumerate(headers):
            field_w, feild_idx = self.get_filter_by_name(header)
            resizer = field_w.resizer_widget

            width = field_w.width()
            if resizer.isVisible():
                width += resizer.width()
            else:
                width -= resizer.width()
            header_view.resizeSection(idx, width)

    def add_filter_field(self, items, label):
        filter_field = PopupFieldLabel(self, items, label)
        self.lay_filters_hor.addWidget(filter_field)
        filter_field.resizer_widget = Resizer(self, filter_field)
        self.lay_filters_hor.addWidget(filter_field.resizer_widget)
        filter_field.field.textChanged.connect(lambda x, y=label:
                                               self.start_filter_table(x, y))

    def start_filter_table(self, text, label):
        header_idx = self.parent().table_view.model.headers.index(label)
        table_proxy_model = self.parent().table_view.proxy_model
        table_proxy_model.setFilterKeyColumn(header_idx)
        table_proxy_model.setFilterWildcard(text)

    def update_popup_list(self, name_widget, items):
        field_w, field_idx = self.get_filter_by_name(name_widget)
        field_w.update_popup_list(items)

    def get_filter_by_name(self, name):
        widgets_count = self.lay_filters_hor.count()
        for i in range(widgets_count):
            w = self.lay_filters_hor.itemAt(i).widget()
            if not isinstance(w, PopupFieldLabel) or w is None:
                continue
            if name == w.name:
                return w, i

    def show_filter(self, name):
        w, idx = self.get_filter_by_name(name)
        w.setVisible(True)
        self._update_layout()

    def hide_filter(self, name):
        w, idx = self.get_filter_by_name(name)
        w.setVisible(False)
        self._update_layout()

    def swap_filters(self, from_idx, to_idx):
        from_idx *= 2
        to_idx *= 2
        # ----------- Swap widgets -----------
        field_w = self.lay_filters_hor.itemAt(from_idx).widget()
        resizer_w = field_w.resizer_widget

        self.lay_filters_hor.removeWidget(field_w)
        self.lay_filters_hor.removeWidget(resizer_w)

        self.lay_filters_hor.insertWidget(to_idx, field_w)
        self.lay_filters_hor.insertWidget(to_idx + 1, resizer_w)
        # ----------- Swap actions -----------
#         header_menu = self.parent().table_view.header_menu
#         action = header_menu.actions()[from_idx]
        self.is_showed = False
        self._update_layout()

    def _update_layout(self):
        """ Arranges the strethces and visibility of fields in layout """
        widgets_count = self.lay_filters_hor.count()
        last_field_found = False
        for i in range(widgets_count - 1, -1, -1):
            w = self.lay_filters_hor.itemAt(i).widget()
            if not isinstance(w, PopupFieldLabel):
                continue

            w.setMaximumWidth(16777215)
            if not w.isVisible():
                w.resizer_widget.setVisible(False)
            else:
                w.resizer_widget.setVisible(True)

            if last_field_found is False and w.isVisible():
                last_field_found = True
                w.resizer_widget.setVisible(False)
                w.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                QtWidgets.QSizePolicy.Preferred)
            else:
                w.setSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                QtWidgets.QSizePolicy.Preferred)
        self._match_with_columns()

    def showEvent(self, event):
        self._update_layout()
#         self.is_showed = False

    def paintEvent(self, event):
        if not self.is_showed:
            self.is_showed = True
            self._match_with_columns()


class Resizer(QtWidgets.QWidget):
    def __init__(self, parent, filter_widget):
        super().__init__(parent)
        self.filter_widget = filter_widget
        self.setFixedSize(10, 10)

        # Palette
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                     QtGui.QColor("#008800"))
        self.setPalette(pal)
        self.setAutoFillBackground(True)

    def mouseMoveEvent(self, event):
        new_width = self.pos().x() - self.filter_widget.pos().x()
        new_pos = QtCore.QPoint(self.mapToParent(event.pos()).x() - self.width() / 2, self.pos().y())
        self.move(new_pos)
        self.filter_widget.setFixedWidth(new_width)
        self.parent()._match_with_columns()
        return QtWidgets.QWidget.mouseMoveEvent(self, event)

