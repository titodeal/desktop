from PySide6 import QtWidgets, QtCore, QtGui
from .table_model import TableModel


class TableView(QtWidgets.QTableView):
    def __init__(self, parent=None, objects=[], headers=[]):
        super().__init__(parent)

        self.setShowGrid(False)

        self.model = TableModel(parent, objects, headers)
        self.proxy_model = QtCore.QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)

        self.setModel(self.proxy_model)

        self.selection_model = self.selectionModel()
        self.set_selection_model()

        self.hheader_view = self.horizontalHeader()
        self.hheader_view.setSectionsMovable(True)
        self.hheader_view.sectionMoved.connect(self.hheader_moved)
        self.vheader_view = self.verticalHeader()

        self.set_hheader_view()

        # ---------- Signals --------------------
        self.clicked.connect(self.current_selection_changed)

    def set_hheader_view(self):
        header = self.hheader_view
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)
        header.setSectionsClickable(False)

        self.setup_header_context_menu()
        header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.exec_header_menu)

    def set_selection_model(self):
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSelectionMode(self.SingleSelection)

    def setup_header_context_menu(self):
        self.header_menu = QtWidgets.QMenu(self.hheader_view)
#         headers = self.model.headers[1:]
        headers = self.model.headers
        for header in headers:
            action = QtGui.QAction(header, self.header_menu)
            action.setCheckable(True)
            action.setChecked(True)
            self.header_menu.addAction(action)

    def exec_header_menu(self, pos):
        act = self.header_menu.exec_(self.mapToGlobal(pos))
        if not act:
            return
        header_idx = self.model.headers.index(act.text())
        logic_idx = self.hheader_view.logicalIndex(header_idx)
        if act.isChecked():
            self.hheader_view.showSection(header_idx)
            self.parent().filters_widget.show_filter(act.text())
        else:
            self.hheader_view.hideSection(header_idx)
            self.parent().filters_widget.hide_filter(act.text())

    def current_selection_changed(self, index):
        self.model.check_item(index)
        print(index.data())

    def get_index_data(self, row, column, role=QtCore.Qt.DisplayRole):
        return self.model.index(row, column).data(role)

    def get_all_column_data(self, column, role=QtCore.Qt.DisplayRole):
        data = []
        row_count = self.model.rowCount()
        for row in range(row_count):
            data.append(self.get_index_data(row, column, role))
        return data

    # ------------ Events ---------------
    def hheader_moved(self, callidx, oldidx, newidx):
        self.parent().filters_widget.swap_filters(oldidx, newidx)

    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            self.selection_model.clearSelection()
            self.selection_model.clearCurrentIndex()
        self.clicked.emit(index)
        return QtWidgets.QTableView.mouseMoveEvent(self, event)

    def focusOutEvent(self, event):
        self.selection_model.clearCurrentIndex()
        self.selection_model.clearSelection()

