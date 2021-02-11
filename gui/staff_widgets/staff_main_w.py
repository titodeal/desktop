from PySide6 import QtWidgets, QtCore
# from .staff_vi_model import StaffViewModel

from gui.project_widgets.project_invite.project_invite_dialog import ProjectInvite
from gui.custom_widgets.table_filters_widget.table_filters_w import TableFiltersWidget


class StaffMainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_vert.setContentsMargins(0, 0, 0, 0)

        # --------- Table Widgete ------------
        headers = ["name", "status", "count", "email"]
        visible_headers = ["status", "name", "email"]
        objs = TempObj.get_list_objects(5)
        self.stuff_table = TableFiltersWidget(self, objs, headers)
#         self.stuff_table.set_hheaders_visible(False)
        self.stuff_table.set_vheaders_visible(False)
        self.stuff_table.set_visible_hheaders(visible_headers)
#         self.stuff_table.set_visible_hheaders([0,1,2])

        # --------- Button ---------------
        self.btn_send_invite = QtWidgets.QPushButton("SEND PROJECT INVITE")
        self.btn_send_invite.clicked.connect(self.open_project_invite)

        # --------- Setup Layouts ---------
        self.lay_main_vert.addWidget(self.btn_send_invite)
        self.lay_main_vert.addWidget(self.stuff_table)

    def open_project_invite(self):
#         self.tst_update_data()
        self.stuff_table.enable_filter_list(True)
#         self.tst()
        return
        curr_user = self.parent().user

        projects = curr_user.projects

        agreements = curr_user.get_agreements()[0]
        agr_contractors = list(filter(lambda x: x.owner_id == curr_user.id,
                               agreements))

        w = ProjectInvite(curr_user.get_server(), projects, agr_contractors, self)
        w.show()

    def tst_update_data(self):
        objs = TempObj.get_list_objects2(10000)
        self.stuff_table.update_table_data(objs)
#     def tst(self):
#         headers = ["name", "status", "count"]
#         objs = TempObj.get_list_objects(5)
#         self.tmp_ftable = TableFiltersWidget(self, objs, headers)
#         self.tmp_ftable.setWindowFlags(QtCore.Qt.Window)
#         self.tmp_ftable.show()

class TempObj:
    def __init__(self, name, status, count, email):
        self.name = name
        self.status = status
        self.count = count
        self.email = email

    @staticmethod
    def get_list_objects(count):
        objs = []
        for i in range(count):
            name = f"name_{i}"
            status = f"status_{i}"
            count = f"{i}"
            email = f"e@mail{i}"
            objs.append(TempObj(name, status, count, email))
        return objs

    @staticmethod
    def get_list_objects2(count):
        objs = []
        for i in range(count):
            name = f"name_{i}_updated"
            status = f"status_{i}_updated"
            count = f"{i}_updated"
            email = f"e@mail{i}_updated"
            objs.append(TempObj(name, status, count, email))
        return objs
