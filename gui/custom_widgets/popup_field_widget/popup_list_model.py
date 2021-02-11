from PySide6 import QtCore


class PopupListModel(QtCore.QStringListModel):
    def __init__(self, items, parent=None):
        super().__init__(items, parent)
        self.items = items

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled \
               | QtCore.Qt.ItemIsSelectable \
               | QtCore.Qt.ItemNeverHasChildren

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.items)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.items[index.row()]

    def update_data(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()
