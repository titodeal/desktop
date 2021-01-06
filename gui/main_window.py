import sys, os
# from app.utils import user
from PySide6 import QtCore, QtWidgets, QtGui

from .utils import window_managment
from .dialogs.sign_dialogs import signin_window


class MainAppWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TiToDeal")
        self.resize(100, 100)

        window_managment.adjust_by_screen(self)


# if __name__ == "__main__":
def start_main_window():
    app = QtWidgets.QApplication(sys.argv)

#     user_server = user.UserSereverCore()


#     if user_server.get_credentials(username, passwd):
#         w = MainAppWindow()
    signin_dialog = signin_window.SignInDialog()
    user_server = signin_dialog.exec_()
    print(user_server)

#     w = MainAppWindow()

#     w.show()
#     button = QtWidgets.QPushButton("HELLO")
#     button.show()
    sys.exit(app.exec_())
