from PySide6 import QtWidgets


class SignupDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_fields_form = QtWidgets.QFormLayout()

        self.lb_inivintation_text = QtWidgets.QLabel("Hello my friend")

        self.login_le = QtWidgets.QLineEdit()
        self.email_le = QtWidgets.QLineEdit()
        self.passwd_le = QtWidgets.QLineEdit()

        self.msgfield_lb = QtWidgets.QLabel()

        self.btn_create_account = QtWidgets.QPushButton("Create account")

        self.btn_create_account.clicked.connect(self.create_account)

        self.lay_fields_form.addRow("Login:", self.login_le)
        self.lay_fields_form.addRow("Email:", self.email_le)
        self.lay_fields_form.addRow("Password:", self.passwd_le)

        self.lay_main_vert.addWidget(self.lb_inivintation_text)
        self.lay_main_vert.addLayout(self.lay_fields_form)
        self.lay_main_vert.addWidget(self.msgfield_lb)
        self.lay_main_vert.addWidget(self.btn_create_account)


    def create_account(self):

        server = self.parent()._get_server()
        if not server:
            self.msgfiled_lb.setText("Error connecting to server.")
            return

        login = self.login_le.text()
        email = self.email_le.text()
        passwd = self.passwd_le.text()

        response = server.create_credentials(login, passwd, email)
        if response[0] is True:
#             main_user.MainUser.server = server
#             self.user = main_user.MainUser(server, login)
#             self.user.update()
            self.accept()
        else:
            self.msgfield_lb.setText(response[1])
            return
