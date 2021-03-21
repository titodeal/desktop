from PySide6 import QtCore


class ProjectsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, projects=[]):
        super().__init__(parent)

        self.projects = projects
        self.headers = ["Name", "Owner", "Status"]
        self.checked = 0

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled \
               | QtCore.Qt.ItemIsSelectable \
               | QtCore.Qt.ItemNeverHasChildren

    def rowCount(self, parent):
        return len(self.projects)

    def columnCount(self, parent):
        return len(self.headers)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return  self.headers[section]

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return self.projects[index.row()].name
            if index.column() == 1:
                return self.projects[index.row()].owner
            if index.column() == 2:
                return self.projects[index.row()].status

        if role == QtCore.Qt.CheckStateRole and index.column() == 0:
            if index.row() == self.checked:
                return QtCore.Qt.Checked
            else:
                return QtCore.Qt.Unchecked

    def check_item(self, index):
        old_checked_index = self.index(self.checked, 0)
        self.checked = index.row()
        self.dataChanged.emit(index, old_checked_index)
