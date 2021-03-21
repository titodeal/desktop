from PySide6 import QtWidgets, QtCore
# from .projects_table_view import ProjectsTableView
# from .filters_widget import FiltersWidget

from gui.custom_widgets. \
     table_filters_widget. \
     table_filters_w import TableFiltersWidget

# import sys, os
# app_path = os.path.abspath("/home/fed/Development/titodeal_desktop")
# sys.path.append(app_path)

from gui.utils import window_managment


class ProjectViewer(QtWidgets.QWidget):
    def __init__(self, parent=None, projects=[]):
        super().__init__(parent)

        self.projects = projects

#         self.setWindowFlag(QtCore.Qt.Window)
#         self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(200, 100)
        window_managment.adjust_by_screen(self)

        # ---------  Layouts ------------------
        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
#         self.lay_header_hori = QtWidgets.QHBoxLayout()

        # ---------  Widgets ------------------
#         self.lb_header_title = QtWidgets.QLabel("Select a project")
#         self.btn_newproject = QtWidgets.QPushButton("NEW PROJECT")
#         self.btn_newproject.clicked.connect(self.get_current_index)
        headers = ["id", "name", "root_folder", "root_id", "owner_id", "status"]
        self.projects_table = TableFiltersWidget(self, self.projects, headers)
#         self.projects_table = ProjectsTableView(self, projects)
#         self.filters_widget = FiltersWidget(self)
#         self.add_filter_fields()

#         # ---------  Setup Layouts ------------------
#         self.lay_header_hori.addWidget(self.lb_header_title, 0, QtCore.Qt.AlignLeft)
#         self.lay_header_hori.addWidget(self.btn_newproject, 0, QtCore.Qt.AlignRight)

#         self.lay_main_vert.addLayout(self.lay_header_hori)
        self.lay_main_vert.addWidget(self.projects_table)
#         self.lay_main_vert.addWidget(self.filters_widget)

        self.lay_main_vert.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
#         window_managment.set_mergins(self, self.lay_header_hori, 0.02, 0.1)

    def add_filter_fields(self):
        headers = self.projects_table.model.headers
        for header in headers:
            self.filters_widget.add_filter_field([f"{header}"])

    def get_current_index(self):
        idx = self.projects_table.selection_model.currentIndex()
        print(idx.data())

# class Project:
#     def __init__(self, properties):
#         self.id = properties["id"]
#         self.name = properties["name"]
#         self.owner = properties["owner"]
#         self.status = properties["status"]


# def get_projects():
#     projects = []
#     for i in range(10):
#         properties = {"id": i,
#                       "name": f"Prj_0{i}",
#                       "owner": f"Owner_0{i}",
#                       "status": "active"}
#         projects.append(Project(properties))
#     return projects
# 
# 
# if __name__ == "__main__":
#     app = QtWidgets.QApplication()
#     w = ProjectViewer(projects=get_projects())
#     w.show()
#     app.exec_()
