from PySide6 import QtWidgets
from gui.custom_widgets.table_filters_widget import table_filters_w


class ContractsTableWidget(table_filters_w.TableFilterScrollArea):
    def __init__(self, parent=None, objects=[]):
        self.headers = ["id",
                        "contractor",
                        "project",
                        "specialty",
                        "role",
                        "accepted",
                        "date" ]
        super().__init__(parent, objects, self.headers)
