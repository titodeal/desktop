from PySide6 import QtCore, QtWidgets


class UserProperties(QtWidgets.QWidget):
#     __user_server = None
    def __init__(self, user, user_server=None, parent=None):
        super().__init__(parent)

        self.user = user
        self.user_server = user_server

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # ----------- Layouts --------------
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_prop_form = QtWidgets.QFormLayout()

        # ----------- Widgets --------------
        # Lable widgets:
        self.id_lb = QtWidgets.QLabel(str(self.user.id))
        self.login_lb = QtWidgets.QLabel(self.user.login)
        self.first_name_lb = QtWidgets.QLabel(self.user.first_name)
        self.last_name_lb = QtWidgets.QLabel(self.user.last_name)
        self.phone_lb = QtWidgets.QLabel(self.user.phone)
        self.email_lb = QtWidgets.QLabel(self.user.email)
        self.relationship = QtWidgets.QLabel("not implemented")

        self.lay_prop_form.addRow("ID:", self.id_lb)
        self.lay_prop_form.addRow("Login:", self.login_lb)
        self.lay_prop_form.addRow("First name:", self.first_name_lb)
        self.lay_prop_form.addRow("Last name:", self.last_name_lb)
        self.lay_prop_form.addRow("Phone:", self.phone_lb)
        self.lay_prop_form.addRow("Email:", self.email_lb)
        self.lay_prop_form.addRow("Realationship:", self.relationship)
        # --
        self.init_buttons()
#         self.btn_send_offer = QtWidgets.QPushButton("Send invintation")
# 
#         # ----------- Signals --------------
#         self.btn_send_offer.clicked.connect(self.send_offer)

        # ----------- Layout setup --------------
        self.lay_main_vert.addLayout(self.lay_prop_form)
#         lay_main_vert.insertWidget(0, self.btn_send_offer)

    def init_buttons(self):
        self.btn_send_offer = QtWidgets.QPushButton("Send invintation")
        if not self.user_server:
            self.btn_send_offer.setEnabled(False)

        # ----------- Signals --------------
        self.btn_send_offer.clicked.connect(self.send_offer)
        # ----------- Layout setup --------------
        self.lay_main_vert.insertWidget(0, self.btn_send_offer)

    def send_offer(self):
        if not self.user_server:
            raise AttributeError("The user properties "
                                 f"'{self.user}' has not server")
        return_status = self.user_server.send_offer(self.user.id)
        if not return_status:
            print("!=> Sending invintation faild: "
                  f"from '{self.user_server.login}' to '{self.user.login}'.")
