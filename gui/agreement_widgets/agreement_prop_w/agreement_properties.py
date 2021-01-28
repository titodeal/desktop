from PySide6 import QtCore, QtWidgets


class AgreementProperties(QtWidgets.QWidget):
#     __user_server = None
    def __init__(self, agreement, user=None, parent=None):
        super().__init__(parent)

        self.agreement = agreement
        self.user = user
        self.server = user.get_server()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # ----------- Layouts --------------
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_prop_form = QtWidgets.QFormLayout()

        # ----------- Widgets --------------
        # Lable widgets:
        self.id_lb = QtWidgets.QLabel(str(self.agreement.id))
        self.owner_lb = QtWidgets.QLabel(self.agreement.owner_login)
        self.contractor_lb = QtWidgets.QLabel(self.agreement.contractor_login)

        status = "accepted" if self.agreement.accepted else "expected"
        self.status_lb = QtWidgets.QLabel(status)
        self.expiration_lb = QtWidgets.QLabel(self.agreement.expiration)

        self.lay_prop_form.addRow("ID:", self.id_lb)
        self.lay_prop_form.addRow("Owner:", self.owner_lb)
        self.lay_prop_form.addRow("contractor", self.contractor_lb)
        self.lay_prop_form.addRow("Status", self.status_lb)
        self.lay_prop_form.addRow("Expiration:", self.expiration_lb)
        # --
        self.init_buttons()
#         self.btn_send_invintation = QtWidgets.QPushButton("Send invintation")
# 
#         # ----------- Signals --------------
#         self.btn_send_invintation.clicked.connect(self.send_invintation)

        # ----------- Layout setup --------------
        self.lay_main_vert.addLayout(self.lay_prop_form)
#         lay_main_vert.insertWidget(0, self.btn_send_invintation)

    def init_buttons(self):
        self.btn_accept = QtWidgets.QPushButton("Accept")
        self.btn_deny = QtWidgets.QPushButton("Deny")
        self.btn_terminate = QtWidgets.QPushButton("Terminate")
        if not self.user:
            self.btn_accept.setEnabled(False)
            self.btn_deny.setEnabled(False)

        # ----------- Signals --------------
        self.btn_accept.clicked.connect(self.accept_offer)
        self.btn_deny.clicked.connect(self.deny_offer)
        self.btn_terminate.clicked.connect(self.terminate_offer)

        # ----------- Layout setup --------------
        if self.agreement.accepted:
                active_btn = self.btn_terminate
        else:
            if self.agreement.owner_id == self.user.id:
                active_btn = self.btn_deny
            else:
                active_btn = self.btn_accept

        self.lay_main_vert.insertWidget(0, active_btn)

    def accept_offer(self):
        self.server.accept_agreement(self.agreement.id)
        pass

    def deny_offer(self):
        pass

    def terminate_offer(self):
        pass
#     def send_invintation(self):
#         if not self.user_server:
#             raise AttributeError("The user properties "
#                                  f"'{self.user}' has not server")
#         return_status = self.user_server.send_invintation(touser_id=self.user.id)
#         if not return_status:
#             print("!=> Sending invintation faild: "
#                   f"from '{self.user_server.login}' to '{self.user.login}'.")
