from PySide6 import QtWidgets

from . import people_tab_widget
from .people_table_view import PeopleTableView
from .userprop_tab_widget import UserPropTabWidget


class PeopleWidget(QtWidgets.QWidget):
    def __init__(self, user, parent=None):
        super().__init__(parent)

#         self.userowner = user
        self.user = user

        self.resize(500, 250)
        self.lay_main_hor = QtWidgets.QHBoxLayout(self)

        # -------------- Widgets -------------------
#         print("=========", self.user.contractors, "===========")
        self.colleagues_tw = PeopleTableView(self.user.contractors, self)

        self.standby_tw = PeopleTableView(self.user.standby_offers, self)

        allusers = self.user.get_all_users()
        self.other_tw = PeopleTableView(allusers, self)

        self.people_tab_widget = people_tab_widget.PeopleTabWidget(self.colleagues_tw,
                                                                   self.standby_tw,
                                                                   self.other_tw,
                                                                   parent=None)

        self.userprop_tab_widget = UserPropTabWidget(self)

        self.lay_main_hor.addWidget(self.people_tab_widget)
        self.lay_main_hor.addWidget(self.userprop_tab_widget)


if __name__ == "__main__":
    import sys
    import os
    app_path = os.path.abspath(".")
    sys.path.append(app_path)

    from gui.people_window import people_table_model
    from gui.people_window import people_tab_widget
    from gui.people_window.people_table_view import  PeopleTableView

    from app.models.user.main_user import MainUser
    from app._lib.server.api import Api

    app = QtWidgets.QApplication(sys.argv)
#     users = [MainUser("User " + str(u)) for u in range(10)]

    server = Api('192.168.88.163', 9090)
    server.get_credentials('User_01', '234')
    MainUser.server = server
    user = MainUser('User_01')
    user.update()

    w = PeopleWidget(user)


    w.show()
    sys.exit(app.exec_())
