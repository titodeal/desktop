from PySide6 import QtWidgets

from .agreement_list_w.agreement_view import AgreementView
from .agreement_list_w.agreement_tabs_w import AgreementTabsW
from .agreement_prop_w.agreement_proptabs_w import AgreementPropTabW


class AgreementMainWidget(QtWidgets.QWidget):
    def __init__(self, user, parent=None):
        super().__init__(parent)

        self.user = user

        self.resize(500, 250)
        self.lay_main_hor = QtWidgets.QHBoxLayout(self)
        self.lay_agreement_vert = QtWidgets.QVBoxLayout()

        # -------------- Widgets -------------------
        self.agreement_prop_section = None
        agreements, offers = self.user.get_agreements()

        self.agreement_view = AgreementView(agreements, self)
        self.offer_view = AgreementView(offers, self)

        self.agreement_list_section = AgreementTabsW(self.agreement_view,
                                               self.offer_view)
        self.agreement_prop_section = AgreementPropTabW(self)

        self.new_agree_btn = QtWidgets.QPushButton("New")

        # -------------- -------------------


        # -------------- Layouts setup -------------------
        self.lay_agreement_vert.addWidget(self.new_agree_btn)
        self.lay_agreement_vert.addWidget(self.agreement_list_section)
        self.lay_main_hor.addLayout(self.lay_agreement_vert)
        self.lay_main_hor.addWidget(self.agreement_prop_section)


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
