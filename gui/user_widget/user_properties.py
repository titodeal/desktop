from PySide6 import QtCore, QtWidgets


class UserProperties(QtWidgets.QWidget):
    def __init__(self, user, parent=None):
        super().__init__(parent)

        self.user = user

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # ----------- Layouts --------------
        lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_prop_form = QtWidgets.QFormLayout()

        # ----------- Widgets --------------
        # Lable widgets:
        self.lb_login = QtWidgets.QLabel(self.user.login)
        self.lb_name = QtWidgets.QLabel("Dmutro")
        self.lb_email = QtWidgets.QLabel(self.user.login)
        self.lb_realationship = QtWidgets.QLabel("coleague")

        self.lay_prop_form.addRow("Login", self.lb_login)
        self.lay_prop_form.addRow("Name", self.lb_name)
        self.lay_prop_form.addRow("Email", self.lb_email)
        self.lay_prop_form.addRow("Realationship", self.lb_realationship)
        # --
        self.btn_send_invintation = QtWidgets.QPushButton("Send invintation")

        # ----------- Signals --------------
        self.btn_send_invintation.clicked.connect(self.send_invintation)

        # ----------- Layout setup --------------
        lay_main_vert.addLayout(self.lay_prop_form)
        lay_main_vert.insertWidget(0, self.btn_send_invintation)

    def send_invintation(self):
        pass

