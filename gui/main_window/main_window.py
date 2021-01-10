
import sys, os
# from app.utils import user
from PySide6 import QtCore, QtWidgets, QtGui

from gui.utils import window_managment
from gui.dialogs.sign_dialogs import signin_window

from gui.people_window import people_main_widget

from .header_pannel import HeaderPannel
from .sidebar import SideBar


class MainAppWindow(QtWidgets.QWidget):
    def __init__(self, user):
        super().__init__()

        self.user = user
        self.server = user.get_user_server()

        self.setWindowTitle("TimeToDeal")
        self.resize(100, 100)

        # -------------- Layouts --------------
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_vert.setContentsMargins(0, 0, 0, 0)

        # -------------- Widgets --------------
        self.header_pannel = HeaderPannel(self)
        self.sidebar = SideBar(name="Side bar", parent=self)
        self.people_widget = people_main_widget.PeopleWidget(user)

        self.TST_LIST = QtWidgets.QListWidget()
#         self.TST_LIST.addItems(["Item_01", "Item_02", "Item_03"])

        # -------------- Signals --------------

        # -------------- Layouts setupt --------------
        self.lay_main_vert.addWidget(self.header_pannel, 0,
                                     QtCore.Qt.AlignTop)
        self.lay_main_vert.addWidget(self.people_widget)
#         self.lay_main_vert.addWidget(self.TST_LIST)

        window_managment.adjust_by_screen(self)

        self.sidebar.set_position()
        self.sidebar.raise_()

        self.tmp_btn = QtWidgets.QPushButton("RUN")
        self.tmp_btn.clicked.connect(self.tmp_click)
        self.lay_main_vert.addWidget(self.tmp_btn)

    def __get_people_data(self):
        collegues = self.user.get_colleagues()
        return []
        return collegues

    def tmp_click(self):
#         collegues = self.user.get_colleagues()
#         from app.models.user.main_user import MainUser
        self.people_widget.update_data()


    def resizeEvent(self, size_event):
        if self.sidebar.isVisible():
            self.sidebar.set_position(size_event.size())



def start_main_window():
    app = QtWidgets.QApplication(sys.argv)

    signin_dialog = signin_window.SignInDialog()

    if signin_dialog.exec_() != 1:
        return
#-----------------------------------------
#     from app._lib.server import api
#     from app.models.user import main_user
#     server = api.Api('192.168.88.163', 9090)
#     server.get_credentials('User_01', '234')
#     user = main_user.MainUser(server, 'User_01')
# #     user.update_user_data()
# 
#     w = MainAppWindow(user)
#-----------------------------------------

    w = MainAppWindow(signin_dialog.user)
    w.show()

    sys.exit(app.exec_())
