from PySide6 import QtWidgets
from .staff_tb_model import StaffListModel


class StaffViewModel(QtWidgets.QListView):
    def __init__(self, parent=None):
        super().__init__(parent)

        ls = ["one", "two", "tree"]
        self.model = StaffListModel(ls, self)
        self.setModel(self.model)
