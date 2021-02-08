from PySide6 import QtCore


class StaffListModel(QtCore.QStringListModel):
    def __init__(self, items, parent=None):
        super().__init__(items, parent)
