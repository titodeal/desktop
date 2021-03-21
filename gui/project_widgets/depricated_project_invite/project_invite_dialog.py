from PySide6 import QtWidgets, QtCore
from gui.utils import window_managment

from gui.custom_widgets. \
     popup_field_widget. \
     popup_field_main import PopupFieldLabel


class ProjectInvite(QtWidgets.QWidget):
    def __init__(self, server, projects, agreements, parent=None):
        super().__init__(parent)

        self.server = server
        self.projects = projects
        self.agreements = agreements

        self.setWindowFlags(QtCore.Qt.Window)
        self.resize(100, 100)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_title_vert = QtWidgets.QVBoxLayout(self)
        self.lay_title_vert.setContentsMargins(15, 15, 0, 50)

        # -------------- Widgets ----------------
        lb_title = QtWidgets.QLabel("Invite user to project")

        self.project_field = PopupFieldLabel(self, self.get_projects_names())
        self.project_field.set_label_text("Project")
        self.project_field.setMinimumWidth(200)

        self.user_field = PopupFieldLabel(self, self.get_contractors_names())
        self.user_field.set_label_text("user/agreement")
        self.user_field.setMinimumWidth(200)

        self.btn_invite = QtWidgets.QPushButton("Invite")

        # -------------- Connects  ----------------
        self.btn_invite.clicked.connect(self.invite)

        # -------------- Lyouts setup ----------------
        self.lay_title_vert.addWidget(lb_title)
        self.lay_main_vert.addLayout(self.lay_title_vert)
        self.lay_main_vert.addWidget(self.project_field, 0, QtCore.Qt.AlignCenter)
        self.lay_main_vert.addWidget(self.user_field, 0, QtCore.Qt.AlignCenter)
        self.lay_main_vert.addWidget(self.btn_invite, 0, QtCore.Qt.AlignRight)
        self.lay_main_vert.addWidget(self.btn_invite, 0, QtCore.Qt.AlignCenter)
        self.lay_main_vert.setSpacing(20)
        self.lay_main_vert.addStretch(1)

        window_managment.adjust_by_screen(self, 2)

    def get_projects_names(self):
        return [x.name for x in self.projects]

    def get_contractors_names(self):
        return [x.contractor_login for x in self.agreements]

    def invite(self):
        project_name = self.project_field.field.text()
        user_name = self.user_field.field.text()
        ids = self.get_userid_projectid(project_name, user_name)
        if not ids:
            return
        project_id = ids[0]
        agreement_id = ids[1]

        self.server.send_contract(project_id, agreement_id)
#         print(project_name, project_id)
#         print(user_name, agreement_id)

    def get_userid_projectid(self, project_name, user_name):
        project_id = -1
        agreement_id = -1

        for prj in self.projects:
            if prj.name == project_name:
                project_id = prj._id
                break

        if project_id == -1:
            print("Incorect project name")
            return

        for agree in self.agreements:
            if agree.contractor_login == user_name:
                agreement_id = agree.id
                break

        if agreement_id == -1:
            print("Incorect user name")
            return
        return (project_id, agreement_id)
