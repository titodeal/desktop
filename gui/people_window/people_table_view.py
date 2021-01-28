from PySide6 import QtCore, QtWidgets

from .people_table_model import PeopleTableModel


class PeopleTableView(QtWidgets.QTableView):

    def __init__(self, users, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.setModel(PeopleTableModel(users))
        self.doubleClicked.connect(self.add_user_tab)

    def selectionChanged(self, item, prev_item):
        try:
            self.parent.userprop_tab_widget.replace_current_user()
        except AttributeError:
            import traceback

            print("=>", traceback.format_exc())

    def add_user_tab(self):
        self.parent.userprop_tab_widget.add_user_tab()
