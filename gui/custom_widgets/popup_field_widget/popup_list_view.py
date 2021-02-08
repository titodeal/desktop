from PySide6 import QtWidgets, QtCore, QtGui

from .popup_list_model import PopupListModel


class PopupListView(QtWidgets.QListView):
    def __init__(self, parent=None, items=[]):
        super().__init__(parent)

        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
#         self.setTabKeyNavigation(True)

        self.list_model = PopupListModel(items, self)
        self.proxy_model = QtCore.QSortFilterProxyModel(self)
        self.proxy_model.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.proxy_model.setSourceModel(self.list_model)

        self.setModel(self.proxy_model)

        self.selection_model = self.selectionModel()

    def set_current_index(self, idx):
        model_index = self.model().index(idx, idx)
        self.selection_model.setCurrentIndex(model_index,
                                             QtCore.QItemSelectionModel.Select)

    def get_current_index(self):
        return self.selection_model.currentIndex()

    def size_item(self):
        idx0 = self.proxy_model.index(0, 0)
        return self.rectForIndex(idx0)

    def row_count(self):
        return self.proxy_model.rowCount()

#     def event(self, event):
#         if event.type() == QtCore.QEvent.WindowActivate:
#             print("Activeated")

        return QtWidgets.QListView.event(self, event)

    def keyPressEvent(self, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if (event.key() == QtCore.Qt.Key_Return) or \
               (event.key() == QtCore.Qt.Key_Enter):

                   print("ENTER")
                   self.parent().set_current_item_value()

        return QtWidgets.QListView.keyPressEvent(self, event)
