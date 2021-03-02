from PySide6 import QtWidgets, QtCore


class SidelistWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, objects=[]):
        super().__init__(parent)

        self.setFixedWidth(250)

        self.lay_main_ver = QtWidgets.QVBoxLayout(self)
        self.lay_main_ver.setContentsMargins(0, 0, 0, 0)
        self.lay_main_ver.setSpacing(0)

        self.list_model = SidelistModel(self, objects)
        self.list_view = QtWidgets.QListView(self)
        self.list_view.setModel(self.list_model)
        self.selection_model = self.list_view.selectionModel()

        self.lay_main_ver.addWidget(self.list_view)


class SidelistModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None, objects=[]):
        super().__init__(parent)
        self.objects = objects

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.objects)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.objects[index.row()].name


