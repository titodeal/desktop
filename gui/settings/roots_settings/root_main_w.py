from PySide6 import QtWidgets

from app.models.root.root_model import RootModel
from .roots_table_w import RootsTableWidget
from .root_properties import RootProperties


class RootsMainWidget(QtWidgets.QWidget):
    def __init__(self, parent, user):
        super().__init__(parent)

        self.name = "Roots"
        self.user = user
        self.server = user.get_server()

        self.lay_main_ver = QtWidgets.QVBoxLayout(self)
        self.lay_main_ver.setContentsMargins(0, 0, 0, 0)

        self.roots = RootModel.get_user_roots(self.server, self.user.id)
#         objects = []
#         objects = RootModel.get_user_roots(server, user.id)
        self.table = RootsTableWidget(self, self.roots)
        self.table.set_first_row_new()
        self.selection_model = self.table.table_view.selection_model

        self.table.table_view.doubleClicked.connect(self.double_clicked_row)
#         self.selection_model.currentChanged.connect(self.current_changed)

        self.lay_main_ver.addWidget(self.table)

#     def current_changed(self, index, pre_index):
#         print(index)

    def double_clicked_row(self, index):
        print(index)
        if index.row() == 0:
            print("NEW ROOT DIALOG")
            root_properties_w = RootProperties(self.user, self)
            root_properties_w.show()
        else:
            root_obj = self.roots[index.row()]
            root_properties_w = RootProperties(self.user, self, root_obj)
            root_properties_w.show()

