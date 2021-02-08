
import sys, os
# from app.utils import user
from PySide6 import QtCore, QtWidgets, QtGui

from gui.dialogs.sign_dialogs import signin_window
from gui.utils import window_managment

from gui.people_window import people_main_widget
from gui.agreement_widgets.agreement_main_w import AgreementMainWidget
from gui.staff_widgets.staff_main_w import StaffMainWidget

from .header_pannel import HeaderPannel
from .sidebar import SideBar


class MainAppWindow(QtWidgets.QWidget):
    def __init__(self, user):
        super().__init__()

        self.user = user
#         self.server = user.get_server()

        self.setWindowTitle("TimeToDeal")
        self.resize(100, 100)

        # -------------- Layouts --------------
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_stacked = QtWidgets.QStackedLayout(self)
        self.lay_main_vert.setContentsMargins(0, 0, 0, 0)
        self.lay_main_stacked.setContentsMargins(0, 0, 0, 0)

        # -------------- Widgets --------------
        self.header_pannel = HeaderPannel(self)
        self.sidebar = SideBar(name="Side bar", parent=self)

        self.agreement_widget = AgreementMainWidget(user)
        self.people_widget = people_main_widget.PeopleWidget(user)
        self.staff_widget = StaffMainWidget(self)

        # -------------- Signals --------------

        # -------------- Layouts setupt --------------
        self.lay_main_stacked.addWidget(self.agreement_widget)
        self.lay_main_stacked.addWidget(self.people_widget)
        self.lay_main_stacked.addWidget(self.staff_widget)
        self.lay_main_vert.addWidget(self.header_pannel, 0,
                                     QtCore.Qt.AlignTop)
        self.lay_main_vert.addLayout(self.lay_main_stacked)


        window_managment.adjust_by_screen(self)

        self.sidebar.set_position()
        self.sidebar.raise_()

        self.tmp_btn = QtWidgets.QPushButton("RUN")
#         self.tmp_btn.clicked.connect(self.tmp_click)
        self.lay_main_vert.addWidget(self.tmp_btn)
        self.lay_main_stacked.setCurrentIndex(2)

    def __get_people_data(self):
        collegues = self.user.get_colleagues()
        return []
        return collegues

#     def tmp_click(self):
#         self.agreements_weedget.update_data()


    def resizeEvent(self, size_event):
        if self.sidebar.isVisible():
            self.sidebar.set_position(size_event.size())



def create_users(server):
    server.create_credentials("Vasul", "123", "vas@gmail.com")
    server.create_credentials("Petro", "123", "pet@gmail.com")
    server.create_credentials("Sonya", "123", "son@gmail.com")
    server.create_credentials("Dmutro", "123", "dmut@gmail.com")

def start_main_window():
    app = QtWidgets.QApplication(sys.argv)

#     signin_dialog = signin_window.SignInDialog()
# # 
#     if signin_dialog.exec_() != 1:
#         return
#-----------------------------------------
    from app._lib.server import api
    from app.models.user import base_user
    server = api.Api('192.168.88.163', 9090)
    server.get_credentials('AndrIi', '123')
    user = base_user.BaseUser('AndrIi', server)
# 
# #     user.update_user_data()
#     create_users(server)

    w = MainAppWindow(user)
#-----------------------------------------

#     w = MainAppWindow(signin_dialog.user)
    w.show()

    sys.exit(app.exec_())