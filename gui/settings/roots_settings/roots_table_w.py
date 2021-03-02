from PySide6 import QtWidgets
from gui.custom_widgets.table_filters_widget import table_filters_w


class RootsTableWidget(table_filters_w.TableFilterScrollArea):
    def __init__(self, parent=None, objects=[]):
        self.headers = ["id",
                        "root_folder",
                        "sharing" ]
        super().__init__(parent, objects, self.headers)
