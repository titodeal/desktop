from PySide6 import QtWidgets, QtCore, QtGui
from gui.custom_widgets.table_filters_widget import table_filters_w
from .dialogs.change_root_dialog import ChangeProjectRootDialog


class ProjectsTableWidget(table_filters_w.TableFilterScrollArea):
    def __init__(self, parent=None, objects=[]):
        self.headers = ["id",
                        "name",
                        "root_folder",
                        "root_id",
                        "owner_id",
                        "status"]

        super().__init__(parent, objects, self.headers)

        if parent and hasattr(parent, "user"):
            self.user = parent.user
            self.server = self.user.get_server()
        else:
            self.user = None
            sefl.server = None

        self.table_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_view.customContextMenuRequested.connect(self.run_context_menu)

    def run_context_menu(self, pos):
        curr_obj = self.get_current_object()
        if curr_obj is None:
            return

        menu = QtWidgets.QMenu(self)
        menu.addAction("Change project root", self.change_root_dialog)
        menu.exec_(QtGui.QCursor().pos())

    def change_root_dialog(self):
        if self.user is None:
            print("=> Unknown init user")
            return


        if self.user.roots:
            w = ChangeProjectRootDialog(self, self.user.roots)
        else:
            w = ChangeProjectRootDialog(self, self.user.get_user_roots())
        result = w.exec_()

        if result == w.Accepted:
            slct_project = self.get_checked_object()

            project_id = slct_project.id
            old_root_id = slct_project.root_id
            new_root_id = w.slct_root.id

            self.server.replace_project_root(project_id, old_root_id, new_root_id)

        elif result == w.Rejected:
            print("No selected")
