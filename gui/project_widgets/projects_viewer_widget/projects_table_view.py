from PySide6 import QtWidgets, QtCore
from projects_table_model import ProjectsTableModel


class ProjectsTableView(QtWidgets.QTableView):
    def __init__(self, parent=None, projects=[]):
        super().__init__(parent)

        self.setModel(ProjectsTableModel(parent, projects))
        self.setShowGrid(False)
        self.set_selection_model()
        self.set_header_view()

    def set_header_view(self):
        header_view = self.horizontalHeader()
        header_view.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header_view.setDefaultAlignment(QtCore.Qt.AlignLeft)
        header_view.setSectionsClickable(False)

    def set_selection_model(self):
        selection_model = self.selectionModel()
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        selection_model.currentChanged.connect(self.current_selection_changed)

    def current_selection_changed(self, index, pre_index):
        self.model().check_item(index)
        print(index)

#         selection_model.setCurrentIndex(self.index(0, 0)
#         print(selection_model.currentIndex()



# class SelectionModel(QtCore.QItemSelectionModel):
#     def __init__(self):
#         super().__init__()

#     def flags(self):
#         return self.Rows
