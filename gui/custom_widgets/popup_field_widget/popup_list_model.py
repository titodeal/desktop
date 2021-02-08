from PySide6 import QtCore


class PopupListModel(QtCore.QStringListModel):
    def __init__(self, items, parent=None):
        super().__init__(items, parent)

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled \
               | QtCore.Qt.ItemIsSelectable \
               | QtCore.Qt.ItemNeverHasChildren
