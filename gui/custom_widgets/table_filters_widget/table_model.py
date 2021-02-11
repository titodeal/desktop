from PySide6 import QtCore


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, objects=[], headers=[]):
        super().__init__(parent)

        self.objects = objects
        self.headers = headers

        self.checkable = False
        self.checked_row = 0

        self._flags = QtCore.Qt.ItemIsEnabled \
                      | QtCore.Qt.ItemIsSelectable \
                      | QtCore.Qt.ItemNeverHasChildren

    def flags(self, index):
        return self._flags

    def set_flags(self, flags):
        self._flags = flags

    def set_checkable(self, _bool):
        self.checkable = _bool

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.objects)

    def columnCount(self, parent):
        return len(self.headers)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return  self.headers[section]
            else:
                return section

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            header = self.headers[index.column()]
            obj = self.objects[index.row()]
            return getattr(obj, header)

        if self.checkable:
            if role == QtCore.Qt.CheckStateRole and index.column() == 0:
                if index.row() == self.checked_row:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked

    def update_data(self, objects):
        self.beginResetModel()
        self.objects = objects
        self.endResetModel()

    def check_item(self, index):
        old_checked_index = self.index(self.checked_row, 0)
        self.checked_row = index.row()
        self.dataChanged.emit(index, old_checked_index)
