import traceback
from PySide6 import QtCore, QtWidgets

from gui.utils import window_managment
from app._lib.server import api

from .signup_window import SignupDialog

import config

from app.models.user import base_user

HOST = config.HOST
PORT = config.PORT

class SignInDialog(QtWidgets.QDialog):
    def __init__(self):
        super(SignInDialog, self).__init__()

#         self.server = None
        self.user = None

        self.setWindowTitle("Sign in dialog")
        self.resize(500, 500)

        # Main layout
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)

        # Widget components
#         self.signin_core_widget = SigninCoreWidget(self)
        self.signin_core_widget = self.signin_core_widget()
        self.btn_logo = QtWidgets.QPushButton("LOGO")
        self.btn_create_account = QtWidgets.QPushButton("Create account")

        self.btn_create_account.clicked.connect(self.create_account)


        # Layout setup
        self.lay_main_vert.addWidget(self.btn_logo, 1,
                                     QtCore.Qt.AlignCenter)

        self.lay_main_vert.addWidget(self.signin_core_widget, 0)
#                                      QtCore.Qt.AlignJustify)

        self.lay_main_vert.addWidget(self.btn_create_account, 1,
                                     QtCore.Qt.AlignCenter)

        window_managment.adjust_by_screen(self)
        mergins_size = self.sizeHint().width() * .25
        margins = QtCore.QMargins(1, 0, 1, 0) * mergins_size
        self.lay_main_vert.setContentsMargins(margins)
        self.setFixedSize(self.size())

#         window_managment.set_mergins(self.signin_core_widget,
#                                      self.signin_core_widget.lay_main_vert,
#                                      0.05, 0.05)
        window_managment.set_mergins(self.signin_core_widget,
                                     self.w_lay_main_vert,
                                     0.05, 0.05)

    def signin_core_widget(self):
        w = QtWidgets.QFrame()
        w.setFrameShape(w.Box)
        w.setFrameShadow(w.Sunken)

        self.w_lay_main_vert = QtWidgets.QVBoxLayout(w)

        # Layout which contains login, password and forgot password elements
        self.lay_loginpasswd_elements = self.setup_signin_form()

        # Widget components 
        self.msgfield_lb = QtWidgets.QLabel("Some field for some text")
        self.btn_signin = QtWidgets.QPushButton("Sign in")

        # Signals
        self.btn_signin.clicked.connect(self.connect_to_server)

        # Layouts setup
        self.w_lay_main_vert.addLayout(self.lay_loginpasswd_elements, 0)

        self.w_lay_main_vert.addWidget(self.msgfield_lb, 0,
                                       QtCore.Qt.AlignHCenter)

        self.w_lay_main_vert.addWidget(self.btn_signin, 1,
                                       QtCore.Qt.AlignCenter)

        return w

    def setup_signin_form(self):
        """Collects the three main elements:
           login field,
           password field and
           forgot password button.
        """
        lay_grid = QtWidgets.QGridLayout()

        # Widget components
        self.login_le = QtWidgets.QLineEdit()
        self.passwd_le = QtWidgets.QLineEdit()

        self.login_label = QtWidgets.QLabel("Login")
        self.passwd_label = QtWidgets.QLabel("Password")

        self.btn_forgot_passwd = QtWidgets.QPushButton("forgot password")


        # Layout setup
        lay_grid.addWidget(self.login_label, 0, 0,
                           QtCore.Qt.AlignRight)
        lay_grid.addWidget(self.login_le, 0, 1)

        lay_grid.addWidget(self.passwd_label, 1, 0,
                           QtCore.Qt.AlignRight)
        lay_grid.addWidget(self.passwd_le, 1, 1)

        lay_grid.addWidget(self.btn_forgot_passwd, 2, 0, 1, 2,
                           QtCore.Qt.AlignRight)

        laebel_offset = self.passwd_label.sizeHint().width()
        lay_grid.setContentsMargins(0, 0, laebel_offset, 0)

        return lay_grid

    def _get_server(self):
        try:
            return api.Api(HOST, PORT, timeout=None)
        except Exception:
            exc = traceback.format_exc()
            print("!=> Error connecting to server. {}", exc)
            return None

    def connect_to_server(self):

        server = self._get_server()
        if not server:
            self.msgfield_lb.setText("Error connecting to server.")
            self.user = None
            return
#         try:
#             server = api.Api(HOST, PORT, timeout=None)
#         except Exception:
#             exc = traceback.format_exc()
#             print("!=> Error connecting to server. {}", exc)
#             self.msgfield_lb.setText("Error connecting to server.")
#             self.user = None
# #             self.server = None
#             return

        login = self.login_le.text()
        passwd = self.passwd_le.text()
        response = server.get_credentials(login, passwd)

        if response[0] is True:
#             base_user.MainUser.server = server
#             self.user = base_user.MainUser(server, login)
            self.user = base_user.BaseUser(login, server)
#             self.user.update_user_data()
            self.accept()
        else:
            self.msgfield_lb.setText(response[1])

    def create_account(self):
        signup_dialog = SignupDialog(self)
        if signup_dialog.exec_():
            self.login_le.setText(signup_dialog.login_le.text())
            self.passwd_le.setText(signup_dialog.passwd_le.text())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    signin_dialog = SignInDialog()
#     result = signin_dialog.exec()
#     print(result)
#     print(signin_dialog.get_data())

    signin_dialog.show()
#     sign_core = SigninCoreWidget()
#     sign_core.show()
#     le = QtWidgets.QLineEdit()
#     wl = line_edit_label("test text", le)
#     wl.show()
    sys.exit(app.exec_())
