from PySide6 import QtWidgets
from app.models.root.root_model import RootModel


class ChangeProjectRootDialog(QtWidgets.QDialog):
    def __init__(self, parent, roots=[]):
        super().__init__(parent)

        self.roots = roots
        self.slct_root = None

        self.lay_main_ver = QtWidgets.QVBoxLayout(self)

        self.cb_root = QtWidgets.QComboBox(self)
        self.cb_root.addItems([r.root_folder for r in roots])
        self.btn_select = QtWidgets.QPushButton("Select")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")

        self.btn_select.clicked.connect(self.accept_)
        self.btn_cancel.clicked.connect(self.reject)
        lay_btn_box = QtWidgets.QHBoxLayout()
        lay_btn_box.addWidget(self.btn_select)
        lay_btn_box.addWidget(self.btn_cancel)

        self.lay_main_ver.addWidget(self.cb_root)
        self.lay_main_ver.addLayout(lay_btn_box)

    def accept_(self):
        self.slct_root = self.roots[self.cb_root.currentIndex()]
        self.accept()
