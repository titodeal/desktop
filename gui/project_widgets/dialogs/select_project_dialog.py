from PySide6 import QtWidgets, QtCore

from ..projects_table_w import ProjectsTableWidget
from .new_project_dialog import NewProjectDialog

class SelectProjectDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, projects=[]):
        super().__init__(parent)

        self.user = self.parent().user
        self.slct_project = None

        self.setWindowFlags(QtCore.Qt.Window)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_header_hori = QtWidgets.QHBoxLayout(self)

        self.lb_header_title = QtWidgets.QLabel("Select a project")
        self.btn_newproject = QtWidgets.QPushButton("NEW PROJECT")
        self.btn_select = QtWidgets.QPushButton("Select")

        self.btn_newproject.clicked.connect(self.start_new_project)
        self.btn_select.clicked.connect(self.select_project)
#         self.project_viewer = ProjectViewer(self, projects)

        self.projects_table = ProjectsTableWidget(self, projects)
        self.projects_table.set_items_checkable(True)

        self.lay_header_hori.addWidget(self.lb_header_title, 0,
                                       QtCore.Qt.AlignLeft)
        self.lay_header_hori.addWidget(self.btn_newproject, 0,
                                       QtCore.Qt.AlignRight)

        self.lay_main_vert.addLayout(self.lay_header_hori)
        self.lay_main_vert.addWidget(self.projects_table)
        self.lay_main_vert.addWidget(self.btn_select)


    def start_new_project(self):
        new_project_d = NewProjectDialog(self.parent().user, self)
        new_project_d.show()

    def select_project(self):
        current_project = self.projects_table.get_checked_object()
        self.slct_project = current_project
        self.accept()
