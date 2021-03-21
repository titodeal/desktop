from PySide6 import QtWidgets, QtCore
from app.models.share.share_model import ShareModel
from app.models.root.root_model import RootModel
from app.models.settings.settings_model import SettingsModel

import os
import platform
from app.utils import cmd_util
from app._lib.titosh_api import titosh_api


class RootProperties(QtWidgets.QDialog):
    def __init__(self, user, parent=None, root_obj=None):
        super().__init__(parent)

        self.root_obj = root_obj
        self.user = user
        self.server = user.get_server()
        self.root_obj = root_obj
        self.new_root_obj = True if root_obj is None else False

        self.setWindowTitle("Root properties")
        self.setWindowFlag(QtCore.Qt.Window)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_vert.setContentsMargins(0, 0, 0, 0)

        self.lay_main_vert.addLayout(self.__lay_root_folder())
        self.lay_main_vert.addWidget(self.__get_lay_sharing())
        self.lay_main_vert.addWidget(self.__buttons_dialog())
#         self.lay_main_vert.addStretch(1)
        if self.root_obj:
            self._match_sharing_data()

    def __lay_root_folder(self):
        lay_form = QtWidgets.QFormLayout()

        self.le_root_folder = QtWidgets.QLineEdit(self)
        self.btn_root_folder = QtWidgets.QPushButton(self)
        self.chbx_sharing = QtWidgets.QCheckBox(self)
        #----------- root field + button layout -----------
        lay_root_field = QtWidgets.QHBoxLayout()
        lay_root_field.setSpacing(0)
        lay_root_field.addWidget(self.le_root_folder)
        lay_root_field.addWidget(self.btn_root_folder)

        self.btn_root_folder.clicked.connect(self.select_root_folder)
        self.chbx_sharing.stateChanged.connect(self.show_hide_sharing_fields)

        lay_form.addRow("Root folder:", lay_root_field)
        lay_form.addRow("Sharing:", self.chbx_sharing)
        return lay_form

    def __buttons_dialog(self):
        buttons = QtWidgets.QDialogButtonBox(self)
        self.btn_save = QtWidgets.QPushButton("Save")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")
        buttons.addButton(self.btn_save, QtWidgets.QDialogButtonBox.ApplyRole)
        buttons.addButton(self.btn_cancel, QtWidgets.QDialogButtonBox.RejectRole)
        self.btn_save.clicked.connect(self.save_data)
        buttons.rejected.connect(self.reject)
        return buttons

    def __get_lay_sharing(self):
        self.group_box_w = QtWidgets.QGroupBox(self)
        lay_middle_form = QtWidgets.QFormLayout(self.group_box_w)
        lay_middle_form.setContentsMargins(QtCore.QMargins(25, 0, 25, 0))

        self.le_host = QtWidgets.QLineEdit()

        self.le_host_root = QtWidgets.QLineEdit()
        self.le_port = QtWidgets.QLineEdit()
        self.le_user = QtWidgets.QLineEdit()
        self.le_passwd = QtWidgets.QLineEdit()

        self.btn_adjust = QtWidgets.QPushButton("adjust")
        self.btn_test = QtWidgets.QPushButton("test")

        self.btn_adjust.clicked.connect(self.adjust_storage_data)
        self.btn_test.clicked.connect(self.titosh_test)

        lay_middle_form.addRow("Storage Host:", self.le_host)
        lay_middle_form.addRow("Host Root:", self.le_host_root)
        lay_middle_form.addRow(self.btn_adjust)
        lay_middle_form.addRow("TiToSH Port:", self.le_port)
        lay_middle_form.addRow("User", self.le_user)
        lay_middle_form.addRow("Password", self.le_passwd)
        lay_middle_form.addRow(self.btn_test)

        #-----------------TEST SHARING FIELDS ------------
#         self.le_share_folder = QtWidgets.QLineEdit()
#         self.btn_share_folder = QtWidgets.QPushButton('Share')
#         self.btn_share_folder.clicked.connect(self.test_share_folder)
#         lay_middle_form.addRow("Share Folder", self.le_share_folder)
#         lay_middle_form.addRow("Share Button", self.btn_share_folder)

        self.group_box_w.hide()
        return self.group_box_w

    def _match_sharing_data(self):
        self.le_root_folder.setText(self.root_obj.root_folder)
        if self.root_obj.sharing:
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked
        self.chbx_sharing.setCheckState(state)

    def show_hide_sharing_fields(self, state):
        if state == QtCore.Qt.Unchecked:
            self.group_box_w.hide()
        else:
            self.group_box_w.show()

    def select_root_folder(self):
        fdialog = QtWidgets.QFileDialog(self)
        fdialog.setFileMode(fdialog.Directory)
        path = fdialog.getExistingDirectory(self, "The Root Project Directory")
        self.le_root_folder.setText(path)

    def adjust_storage_data(self):
        root_folder = os.path.normpath(self.le_root_folder.text())

        if  not os.path.exists(root_folder):
            print(f"!=> The path '{root_folder}' does not exists.")
            return

        path = root_folder
        if platform.system() == "Linux":
            while path:
                print(path)
                cmd = f"mount | \
                        cut --delimiter=' ' --fields=1,3 | \
                        grep -E {path}$"
                code, mount, err_msg = cmd_util.run_subprosess(cmd)
                if code == 0:
                    host, localhost = mount.split(" ")
                    host, folder = host.split(":")

                    local_tail = root_folder.replace(localhost, "")
                    host_root = "".join([folder, local_tail])

                    self.le_host.setText(host)
                    self.le_host_root.setText(host_root)
                    return
                path = "/".join(path.split(os.sep)[:-1])

        print("IT IS LOCALHOST")
        self.le_host.setText("localhost")
        self.le_host_root.setText(root_folder)

    def titosh_test(self):
        host = self.le_host.text()
        port = int(self.le_port.text())
        user = self.le_user.text()
        passwd = self.le_passwd.text()
        root_folder = self.le_host_root.text()
        response = titosh_api.mount_fs(host, port, user, passwd, root_folder )
        print("RESPONSE = ", response)

#     def test_share_folder(self):
    def sharing_data_correctly(self):
        lay_share_data = self.group_box_w.layout()
        fields_count = lay_share_data.count()
        all_filled = True

        for idx in range(fields_count):
            widget = lay_share_data.itemAt(idx).widget()
            label = lay_share_data.labelForField(widget)
            if isinstance(widget, QtWidgets.QLineEdit):
                if not widget.text():
                    print(f"!=> The field '{label.text()}' must by filled")
                    all_filled = False
        if not all_filled:
            return

        local_root_folder = self.le_root_folder.text()
        host = self.le_host.text()
        port = int(self.le_port.text())

        user = self.le_user.text()
        passwd = self.le_passwd.text()
        root_folder = self.le_host_root.text()

        if  not os.path.exists(local_root_folder):
            print(f"!=> The path '{local_root_folder}' does not exists.")
            return

        cmd = f"ping -c 1 {host}"
        code, mount, err_msg = cmd_util.run_subprosess(cmd)
        if code != 0:
            print(f"!=> The Storage host '{host}' does not available")
            return

        cmd = f"ping -c 1 {host}"
        code, mount, err_msg = cmd_util.run_subprosess(cmd)
        if code != 0:
            print(f"!=> The Storage host '{host}' does not available")
            return

        cmd = f"nc -zv {host} {port}"
        code, mount, err_msg = cmd_util.run_subprosess(cmd)
        if code != 0:
            print(f"!=> The TiToSh service does not available on port '{port}'")
            return

        status, msg = titosh_api.check_storage_folder(host,
                                                   port,
                                                   user,
                                                   passwd,
                                                   root_folder)
        if status is False:
            print(msg)
            return False

        return True

#         print("RESPONSE = ", response)

#                 print(widget)
#             if isinstance(label, QtWidgets.QLabel):
#                 print(label.text())
#         storage = self.le_host.text()
#         storage_root = self.le_host_root.text()
#         titosh_port = self.le_port.text()
#         user = self.le_user.text()
#         passwd = self.le_passwd.text()


#     def test_share_folder(self):
#         folder = self.le_share_folder.text()
#         response = titosh_api.share_folder(host, port, user, passwd, root_folder )
#         print("RESPONSE = ", response)

    def save_data_nosharing(self):
        status, data = self.server.create_user_root(self.user.id,
                                                    self.le_root_folder.text(),
                                                    sharing=False)
        if status is False:
            print("Save data failed: ", data)
            return
        else:
            print("Save data successfull: ", data)

    def save_data_sharing(self):
        if not self.sharing_data_correctly():
            return

        # Creating new root object in database.
        if self.new_root_obj:
            status, data = self.server.create_user_root(
                                self.user.id,
                                self.le_root_folder.text(),
                                sharing=True
                                )
            if status is False:
                print("Save data failed: ", data)
                return
            else:
                root_id = data[0]['root_id']

        # In case the sharing option has changed it
        # updates the existing root object in database.
        else:
            root_id = self.root_obj.id
            if self.root_obj.sharing is False:
                self.server.update_root(root_id, sharing=True)

        status, data = titosh_api.mount_fs(
                                           self.le_host.text(),
                                           int(self.le_port.text()),
                                           self.le_user.text(),
                                           self.le_passwd.text(),
                                           self.le_host_root.text()
                                          )
        if status is False:
            print("Save data failed: ", data)
            return

        # Saving share object.
        share_obj = ShareModel(root_id,
                               self.le_host.text(),
                               self.le_host_root.text(),
                               self.le_user.text(),
                               self.le_passwd.text())

        settings = SettingsModel()
        settings.setValue(f"share/{root_id}", share_obj)
        settings.sync()

    def save_data(self):
        if self.chbx_sharing.checkState() == QtCore.Qt.Checked:
            self.save_data_sharing()
        else:
            self.save_data_nosharing()
