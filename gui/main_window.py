import sys, os
# from app.utils import user
from PySide6 import QtCore, QtWidgets, QtGui

from .utils import window_managment
from .dialogs.sign_dialogs import signin_window


class MainAppWindow(QtWidgets.QWidget):
    def __init__(self, server):
        super().__init__()
        self.setWindowTitle("TiToDeal")
        self.resize(100, 100)

        window_managment.adjust_by_screen(self)

        server.del_user("test_user")


def start_main_window():
    app = QtWidgets.QApplication(sys.argv)

    signin_dialog = signin_window.SignInDialog()
    result = signin_dialog.exec_()

    if result != 1:
        return

    w = MainAppWindow(signin_dialog.server)
    w.show()
    sys.exit(app.exec_())
