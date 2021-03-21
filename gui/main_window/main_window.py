
import sys, os
# from app.utils import user
from PySide6 import QtCore, QtWidgets, QtGui

from gui.dialogs.sign_dialogs import signin_window
from gui.utils import window_managment

from gui.people_window import people_main_widget
from gui.agreement_widgets.agreement_main_w import AgreementMainWidget
# from gui.staff_widgets.staff_main_w import StaffMainWidget
from gui.contracts_widgets.contracts_main_w import ContractsMainWidget

from .header_pannel import HeaderPannel
from .sidebar import SideBar

import config as conf

TITOD_HOST = conf.HOST
TITOD_PORT = conf.PORT


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
#         self.staff_widget = StaffMainWidget(self)
        self.contracts_widget = ContractsMainWidget(self, user)

        # -------------- Signals --------------

        # -------------- Layouts setupt --------------
        self.lay_main_stacked.addWidget(self.agreement_widget)
        self.lay_main_stacked.addWidget(self.people_widget)
#         self.lay_main_stacked.addWidget(self.staff_widget)
        self.lay_main_stacked.addWidget(self.contracts_widget)
        self.lay_main_vert.addWidget(self.header_pannel, 0,
                                     QtCore.Qt.AlignTop)
        self.lay_main_vert.addLayout(self.lay_main_stacked)


        window_managment.adjust_by_screen(self)

        self.sidebar.set_position()
        self.sidebar.raise_()

        self.tmp_btn = QtWidgets.QPushButton("RUN")
        self.tmp_btn.clicked.connect(self.tmp_click)
        self.lay_main_vert.addWidget(self.tmp_btn)
        self.lay_main_stacked.setCurrentIndex(2)

    def __get_people_data(self):
        collegues = self.user.get_colleagues()
        return []
        return collegues

    #################  TEMP ############################
    def tmp_click(self):
        from app.models.settings.settings_model import SettingsModel
        root_id = self.user.current_project.root_id
        settings = SettingsModel()
        print("Storage Host:", settings.value(f"share/{root_id}").storage_host)
        print("Storage Root:", settings.value(f"share/{root_id}").storage_root)
        print(settings.contains("share/8"))
#         self.agreements_weedget.update_data()
#         curr_project = self.user.current_project
#         print(curr_project.root)

    ####################################################


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
    from app.models.user.user import User
    server = api.Api(TITOD_HOST, TITOD_PORT)
    server.get_credentials('AndrIi', '123')
    user = User.init_user(server)
    user.set_current_project()
# 
# #     user.update_user_data()
#     create_users(server)

    w = MainAppWindow(user)
#-----------------------------------------

#     w = MainAppWindow(signin_dialog.user)
    w.show()

    sys.exit(app.exec_())
