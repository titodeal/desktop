from PySide6 import QtWidgets, QtCore, QtGui
from .projects_table_model import ProjectsTableModel


class ProjectsTableView(QtWidgets.QTableView):
    def __init__(self, parent=None, projects=[]):
        super().__init__(parent)

        self.model = ProjectsTableModel(parent, projects)
        self.proxy_model = QtCore.QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)

        self.setModel(self.proxy_model)

        self.selection_model = self.selectionModel()
        self.set_selection_model()

        self.header_view = self.horizontalHeader()
        self.set_header_view()

        self.setShowGrid(False)

    def set_header_view(self):
        header = self.header_view
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)
        header.setSectionsClickable(False)

        self.setup_header_context_menu()
        header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.exec_header_menu)

    def set_selection_model(self):
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.selection_model.currentChanged.connect(self.current_selection_changed)

    def setup_header_context_menu(self):
        self.header_menu = QtWidgets.QMenu(self.header_view)
        headers = self.model.headers[1:]
        for header in headers:
            action = QtGui.QAction(header, self.header_menu)
            action.setCheckable(True)
            action.setChecked(True)
            self.header_menu.addAction(action)

    def exec_header_menu(self, pos):
        act = self.header_menu.exec_(self.mapToGlobal(pos))
        header_idx = self.model.headers.index(act.text())
        if act.isChecked():
            self.header_view.showSection(header_idx)
            self.parent().filters_widget.show_widget(header_idx)
        else:
            self.header_view.hideSection(header_idx)
            self.parent().filters_widget.hide_widget(header_idx)
        print(header_idx)

    def current_selection_changed(self, index, pre_index):
        self.model.check_item(index)
        print(index.data())
