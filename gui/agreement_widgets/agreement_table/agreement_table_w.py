from PySide6 import QtWidgets, QtCore
from gui.custom_widgets.table_filters_widget.table_filters_w import TableFilterScrollArea


class AgreementsTable(QtWidgets.QWidget):
    def __init__(self, parent=None, objects=[]):
        super().__init__(parent)

        self.setWindowFlags(QtCore.Qt.Window)

        self.headers = ["id",
                        "login",
                        "type",
                        "accepted",
                        "conditions",
                        "expiration"]

        self.lay_main_vert = QtWidgets.QVBoxLayout(self)
        self.lay_main_vert.setContentsMargins(0, 0, 0, 0)

        self.table = TableFilterScrollArea(self, objects, self.headers)
        self.set_items_checkable = self.table.set_items_checkable

        self.lay_main_vert.addWidget(self.table)
