from PySide6 import QtWidgets, QtCore, QtGui
from .table_model import TableModel


class TableView(QtWidgets.QTableView):
    def __init__(self, parent=None, objects=[], headers=[]):
        super().__init__(parent)

        self.setShowGrid(False)

        # ------------ Table Model ------------
        self.model = TableModel(parent, objects, headers)
        # ------------ Proxy Model ------------
        self.proxy_model = QtCore.QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)

        self.setModel(self.proxy_model)

        # ------------ Selection Model ------------
        self.selection_model = self.selectionModel()
        self._set_selection_model()

        # ------------ Header Views ------------
        self.hheader = self.horizontalHeader()
        self.vheader = self.verticalHeader()
        self.vheader.pre_width = 0
        self._set_hheader()

        # ------------ Scroll Bar ------------
        self.vscroll = self.verticalScrollBar()
        self.vscroll.visibility = False
        self.hscroll = self.horizontalScrollBar()
        self.hscroll.setVisible(False)

        # ---------- Signals --------------------
        self.clicked.connect(self.current_selection_changed)

    def _set_selection_model(self):
        """ Setup for selection model """
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSelectionMode(self.SingleSelection)

    def _set_hheader(self):
        """ Setup for horizontal headers """
        header = self.hheader
        header.setSectionsMovable(True)
        header.setFirstSectionMovable(False)
        header.sectionMoved.connect(self.hheader_moved)

        header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

        header.setStretchLastSection(True)
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)
        header.setSectionsClickable(False)

        self._setup_header_context_menu()
        header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self._exec_header_menu)

    def _setup_header_context_menu(self):
        self.header_menu = QtWidgets.QMenu(self.hheader)
        headers = self.model.headers
        for header in headers:
            action = QtGui.QAction(header, self.header_menu)
            action.setCheckable(True)
            action.setChecked(True)
            self.header_menu.addAction(action)

    def _exec_header_menu(self, pos):
        act = self.header_menu.exec_(self.mapToGlobal(pos))
        if not act:
            return
        header_idx = self.model.headers.index(act.text())
#         logic_idx = self.hheader.logicalIndex(header_idx)
        if act.isChecked():
            self.hheader.showSection(header_idx)
            self.parent().filters_widget.show_filter(act.text())
        else:
            if self.hheader.hiddenSectionCount() == self.hheader.count() - 1:
                act.setChecked(True)
                return
            self.hheader.hideSection(header_idx)
            self.parent().filters_widget.hide_filter(act.text())

    def current_selection_changed(self, index):
        self.model.check_item(index)
        print(index.data())

    def get_all_column_data(self, column, role=QtCore.Qt.DisplayRole):
        data = []
        row_count = self.model.rowCount()
        for row in range(row_count):
            data.append(self.get_index_data(row, column, role))
        return data

    def get_index_data(self, row, column, role=QtCore.Qt.DisplayRole):
        return self.model.index(row, column).data(role)

    # ------------ Events ---------------
    def hheader_moved(self, callidx, oldidx, newidx):
        self.parent().filters_widget.swap_filters(oldidx, newidx)

    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            self.selection_model.clearSelection()
            self.selection_model.clearCurrentIndex()
        self.clicked.emit(index)
        event.ignore()
        return QtWidgets.QTableView.mousePressEvent(self, event)

    def focusOutEvent(self, event):
        return QtWidgets.QTableView.focusOutEvent(self, event)
#         self.selection_model.clearCurrentIndex()
#         self.selection_model.clearSelection()

    def paintEvent(self, event):
        # ----- Alignt the filters field -----
        self.adjust_filters_area()
        return QtWidgets.QTableView.paintEvent(self, event)

    def adjust_filters_area(self):
        """ Align the filters fields with the table widget """
        vheader_width = self.vheader.width()
        vscroll_width = self.vscroll.width()
        if vheader_width != self.vheader.pre_width:
            self.vheader.pre_width = vheader_width
            self.parent().filters_widget.adjust_front_space(vheader_width)
        if self.vscroll.isVisible() != self.vscroll.visibility:
            self.vscroll.visibility = self.vscroll.isVisible()
            last_space = 0 if self.vscroll.visibility is False else vscroll_width
            self.parent().filters_widget.adjust_last_space(last_space)
