from PySide6 import QtWidgets, QtCore

from ..projects_viewer_widget.project_viewer import ProjectViewer
from .new_project_dialog import NewProjectDialog

class SelectProjectDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, projects=[]):
        super().__init__(parent)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_header_hori = QtWidgets.QHBoxLayout(self)

        self.lb_header_title = QtWidgets.QLabel("Select a project")
        self.btn_newproject = QtWidgets.QPushButton("NEW PROJECT")
        self.btn_newproject.clicked.connect(self.start_new_project)
        self.project_viewer = ProjectViewer(self, [])

        self.lay_header_hori.addWidget(self.lb_header_title, 0,
                                       QtCore.Qt.AlignLeft)
        self.lay_header_hori.addWidget(self.btn_newproject, 0,
                                       QtCore.Qt.AlignRight)

        self.lay_main_vert.addLayout(self.lay_header_hori)
        self.lay_main_vert.addWidget(self.project_viewer)


    def start_new_project(self):
        new_project_d = NewProjectDialog(self.parent().user, self)
        new_project_d.show()

