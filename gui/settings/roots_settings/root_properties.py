from PySide6 import QtWidgets, QtCore


class RootProperties(QtWidgets.QDialog):
    def __init__(self, user, parent=None, root_obj=None):
        super().__init__(parent)

        self.root_obj = root_obj
        self.user = user
        self.server = user.get_server()

        self.setWindowTitle("Root properties")
        self.setWindowFlag(QtCore.Qt.Window)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_vert.setContentsMargins(0, 0, 0, 0)
        self.lay_form = QtWidgets.QFormLayout()

        self.le_root_folder = QtWidgets.QLineEdit(self)
        self.chbx_sharing = QtWidgets.QCheckBox(self)

        self.btn_root_folder = QtWidgets.QPushButton(self)
        lay_root_folder = QtWidgets.QHBoxLayout()
        lay_root_folder.setSpacing(0)
        lay_root_folder.addWidget(self.le_root_folder)
        lay_root_folder.addWidget(self.btn_root_folder)

        self.btn_root_folder.clicked.connect(self.select_root_project)
        self.chbx_sharing.stateChanged.connect(self.change_sharing_chbx)
        self.btn_save = QtWidgets.QPushButton("Save")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")

        self.buttons = QtWidgets.QDialogButtonBox(self)
        self.buttons.addButton(self.btn_save, QtWidgets.QDialogButtonBox.ApplyRole)
        self.buttons.addButton(self.btn_cancel, QtWidgets.QDialogButtonBox.RejectRole)
        self.btn_save.clicked.connect(self.save_data)
        self.buttons.rejected.connect(self.reject)


        self.lay_form.addRow("Root folder:", lay_root_folder)
        self.lay_form.addRow("Sharing:", self.chbx_sharing)
#         self.lay_form.addRow("Sharing:", self.le_root_folder)
        self.lay_main_vert.addLayout(self.lay_form)
        self.lay_main_vert.addWidget(self.get_lay_sharing())
        self.lay_main_vert.addWidget(self.buttons)

        if self.root_obj:
            self.enter_data_object()

    def get_lay_sharing(self):
        self.group_box_w = QtWidgets.QGroupBox(self)
        lay_middle_form = QtWidgets.QFormLayout(self.group_box_w)
        lay_middle_form.setContentsMargins(QtCore.QMargins(25, 0, 25, 0))

        self.le_ip = QtWidgets.QLineEdit()

        self.le_mount = QtWidgets.QLineEdit()
        self.le_port = QtWidgets.QLineEdit()
        self.le_user = QtWidgets.QLineEdit()
        self.le_passwd = QtWidgets.QLineEdit()

        self.btn_adjust = QtWidgets.QPushButton("adjust")
        self.btn_test = QtWidgets.QPushButton("test")

        lay_middle_form.addRow("Storage IP:", self.le_ip)
        lay_middle_form.addRow("Mount:", self.le_mount)
        lay_middle_form.addRow(self.btn_adjust)
        lay_middle_form.addRow("TiToSH Port:", self.le_port)
        lay_middle_form.addRow("User", self.le_user)
        lay_middle_form.addRow("Passwork", self.le_passwd)
        lay_middle_form.addRow(self.btn_test)

        return self.group_box_w

    def enter_data_object(self):
        self.le_root_folder.setText(self.root_obj.root_folder)
        if self.root_obj.sharing:
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked
        self.chbx_sharing.setCheckState(state)

    def change_sharing_chbx(self, state):
        if state == QtCore.Qt.Unchecked:
            self.group_box_w.hide()
            print("Unchecked")
        else:
            self.group_box_w.show()
            print("checked")

    def select_root_project(self):
        fdialog = QtWidgets.QFileDialog(self)
        fdialog.setFileMode(fdialog.Directory)
        path = fdialog.getExistingDirectory(self, "The Root Project Directory")
        self.le_root_folder.setText(path)

    def save_data(self):
        isshare = self.chbx_sharing.checkState()
        sharing = True if isshare == QtCore.Qt.Checked else False
        if not self.root_obj:
            root_folder = self.le_root_folder.text()
            self.server.create_user_root(self.user.id, root_folder, sharing)
        else:
            if sharing is not self.root_obj.sharing:
                self.server.update_root_sharing(user_id, sharing)

        print("Savoing Data")

#     def select_root_project(self):
#         print("OPEN BROWSE DIALOG")
