import sys, os
from PySide6 import QtCore, QtWidgets, QtGui

app_path = os.path.abspath(".")
sys.path.append(app_path)
from gui.utils import window_managment


class SignInDialog(QtWidgets.QDialog):
    def __init__(self):
        super(SignInDialog, self).__init__()
        self.setWindowTitle("Sign in dialog")
        self.resize(500, 500)

        # Main layout
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)

        # Widget components
        self.signin_core_widget = SigninCoreWidget(self)
        self.btn_logo = QtWidgets.QPushButton("LOGO")
        self.btn_create_account = QtWidgets.QPushButton("Create account")


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

        window_managment.set_mergins(self.signin_core_widget,
                                     self.signin_core_widget.lay_main_vert,
                                     0.05, 0.05)


#     def signin_core_widget(self):
#         w = QtWidgets.QFrame()
#         w.setFrameShape(self.Box)
#         w.setFrameShadow(self.Sunken)
# 
#         self.w_lay_main_vert = QtWidgets.QVBoxLayout(self)
# 
#         # Layout which contains login, password and forgot password elements
#         self.lay_loginpasswd_elements = self.setup_signin_form()
# 
#         # Widget components 
#         self.label_msg_field = QtWidgets.QLabel("Some field for some text")
#         self.btn_signin = QtWidgets.QPushButton("Sign in")
# 
#         # Signals
#         self.btn_signin.clicked.connect(self.connect_to_server)
# 
#         # Layouts setup
#         self.lay_main_vert.addLayout(self.lay_loginpasswd_elements, 0)
# 
#         self.lay_main_vert.addWidget(self.label_msg_field, 0,
#                                      QtCore.Qt.AlignHCenter)
# 
#         self.lay_main_vert.addWidget(self.btn_signin, 1,

class SigninCoreWidget(QtWidgets.QFrame):
    """Represents main elements to sign in."""
    def __init__(self, parent=None):
        super(SigninCoreWidget, self).__init__(parent)

        self.setFrameShape(self.Box)
        self.setFrameShadow(self.Sunken)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)

        # Layout which contains login, password and forgot password elements
        self.lay_loginpasswd_elements = self.setup_signin_form()

        # Widget components 
        self.label_msg_field = QtWidgets.QLabel("Some field for some text")
        self.btn_signin = QtWidgets.QPushButton("Sign in")

        # Signals
        self.btn_signin.clicked.connect(self.connect_to_server)

        # Layouts setup
        self.lay_main_vert.addLayout(self.lay_loginpasswd_elements, 0)

        self.lay_main_vert.addWidget(self.label_msg_field, 0,
                                     QtCore.Qt.AlignHCenter)

        self.lay_main_vert.addWidget(self.btn_signin, 1,
                                     QtCore.Qt.AlignCenter)

    def setup_signin_form(self):
        """Collects the three main elements:
           login field,
           password field and
           forgot password button.
        """
        lay_grid = QtWidgets.QGridLayout()

        # Widget components
        self.login_lineedit = QtWidgets.QLineEdit()
        self.passwd_lineedit = QtWidgets.QLineEdit()

        self.login_label = QtWidgets.QLabel("Login")
        self.passwd_label = QtWidgets.QLabel("Password")

        self.btn_forgot_passwd = QtWidgets.QPushButton("forgot password")

        # Layout setup
        lay_grid.addWidget(self.login_label, 0, 0,
                           QtCore.Qt.AlignRight)
        lay_grid.addWidget(self.login_lineedit, 0, 1)

        lay_grid.addWidget(self.passwd_label, 1, 0,
                           QtCore.Qt.AlignRight)
        lay_grid.addWidget(self.passwd_lineedit, 1, 1)

        lay_grid.addWidget(self.btn_forgot_passwd, 2, 0, 1, 2,
                           QtCore.Qt.AlignRight)

        laebel_offset = self.passwd_label.sizeHint().width()
        lay_grid.setContentsMargins(0, 0, laebel_offset, 0)

        return lay_grid

    def connect_to_server(self):
        pass


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
