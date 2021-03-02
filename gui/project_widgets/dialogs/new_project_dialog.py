from PySide6 import QtWidgets, QtCore
from gui.utils import window_managment
from app.models.root.root_model import RootModel


class NewProjectDialog(QtWidgets.QDialog):
    def __init__(self, user, parent=None):
        super().__init__(parent)

        self.user = user
        self.server = user.get_server()
        self.roots = RootModel.get_user_roots(self.server, self.user.id)

        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(100, 100)
        window_managment.adjust_by_screen(self, 1.6)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_header = self.get_lay_header()
        self.lay_middle_form = self.get_lay_middle()
        self.lay_floor = self.get_lay_floor()

        self.lay_main_vert.addLayout(self.lay_header)
        self.lay_main_vert.addLayout(self.lay_middle_form)
        self.lay_main_vert.addLayout(self.lay_floor)
        self.lay_main_vert.addStretch()

    def get_lay_header(self):
        lay_header = QtWidgets.QHBoxLayout()
        lay_header.setContentsMargins(QtCore.QMargins(12, 12, 12, 25))
        title = QtWidgets.QLabel("NEW PROJECT")
        lay_header.addWidget(title)
#         lay_header.addWidget(title, 0, QtCore.Qt.AlignTop)
        return lay_header

    def get_lay_middle(self):
        lay_middle_form = QtWidgets.QFormLayout()
        lay_middle_form.setContentsMargins(QtCore.QMargins(25, 0, 25, 0))

        self.le_name = QtWidgets.QLineEdit()
        self.cb_scheme = QtWidgets.QComboBox(self)
        self.cb_scheme.addItems(["Root=>Series=>Episode=>Shot",
                                 "Root=>Episode=>Shot"])
        self.le_fps = QtWidgets.QLineEdit()


#         root_paths = [obj.root_folder for obj in self.roots]
        self.cb_root_project = QtWidgets.QComboBox(self)
        for idx, obj in enumerate(self.roots):
            self.cb_root_project.addItem(obj.root_folder)
            self.cb_root_project.setItemData(idx, str(obj.id))
#             print(self.cb_root_project.currentData(QtCore.Qt.UserRole))
#         self.cb_root_project.addItems(root_paths)

#         self.le_root_project = QtWidgets.QLineEdit()
        self.btn_root_project = QtWidgets.QPushButton("...")
#         self.btn_root_project.setFixedWidth(30)
#         lay_root_project = QtWidgets.QHBoxLayout()
#         lay_root_project.addWidget(self.le_root_project)
#         lay_root_project.addWidget(self.btn_root_project)
#         lay_root_project.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
#         lay_root_project.setSpacing(0)
#         self.btn_root_project.clicked.connect(self.select_root_project)

        lay_middle_form.addRow("Name:", self.le_name)
        lay_middle_form.addRow("Scheme:", self.cb_scheme)
        lay_middle_form.addRow("FPS:", self.le_fps)
        lay_middle_form.addRow("Root project:", self.cb_root_project)

        return lay_middle_form

    def get_lay_floor(self):
        lay_btn_dialog = QtWidgets.QHBoxLayout()
        lay_btn_dialog.setContentsMargins(QtCore.QMargins(0, 25, 0, 0))

        self.btn_create = QtWidgets.QPushButton("Create")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")

        self.btn_create.clicked.connect(self.create_project)
        self.btn_cancel.clicked.connect(self.reject)

        lay_btn_dialog.addWidget(self.btn_cancel, 1,
                                 QtCore.Qt.AlignRight)
        lay_btn_dialog.addWidget(self.btn_create, 0,
                                 QtCore.Qt.AlignRight)


        return lay_btn_dialog

    def select_root_project(self):
        fdialog = QtWidgets.QFileDialog(self)
        fdialog.setFileMode(fdialog.Directory)
        path = fdialog.getExistingDirectory(self, "The Root Project Directory")
        self.le_root_project.setText(path)

    def create_project(self):

        if self.cb_scheme.currentText() == "Root=>Series=>Episode=>Shot":
            scheme = "SES"
        else:
            scheme = "SE"

        root_id = self.cb_root_project.currentData(QtCore.Qt.UserRole)
#         root_folder = self.cb_root_project.currentData(QtCore.Qt.UserRole)
        args = {"project_name": self.le_name.text(),
                "owner_id": self.user.id,
                "root_id": self.cb_root_project.currentData(role=QtCore.Qt.UserRole),
                "scheme": scheme,
                "fps": self.le_fps.text(),
                "status": "new"}

        print(self.cb_root_project.currentData())
        print("ARGS ===================", args)

        self.server.create_project(**args)
