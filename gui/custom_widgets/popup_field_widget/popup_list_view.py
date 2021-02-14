from PySide6 import QtWidgets, QtCore, QtGui

from .popup_list_model import PopupListModel


class PopupListView(QtWidgets.QListView):
    def __init__(self, parent=None, items=[]):
        super().__init__(parent)

        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)

        self.model = PopupListModel(items, self)
        self.proxy_model = QtCore.QSortFilterProxyModel(self)
        self.proxy_model.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.proxy_model.setSourceModel(self.model)

        self.setModel(self.proxy_model)

        self.selection_model = self.selectionModel()

    def get_selected_index(self):
        if not self.model.rowCount() > 0:
            return QtCore.QModelIndex()
        if not self.selection_model.hasSelection():
            self.set_selection(0)
        return self.selection_model.selectedIndexes()[0]

    def set_selection(self, rowidx, colidx=0):
        model_index = self.model.index(rowidx, colidx)
        self.selection_model.select(model_index,
                                    QtCore.QItemSelectionModel.Select)
        self.selection_model.setCurrentIndex(model_index,
                                    QtCore.QItemSelectionModel.Select)

    def select_next_item(self):
        if not self.selection_model.hasSelection():
            self.set_selection(0)
        else:
            cur_idx = self.get_selected_index().row()
            self.selection_model.clearSelection()
            self.set_selection(cur_idx + 1)

    def size_item(self):
        idx0 = self.proxy_model.index(0, 0)
        return self.rectForIndex(idx0)

    def row_count(self):
        return self.proxy_model.rowCount()

    def closeEvent(self, event):
        self.selection_model.clearSelection()
        self.selection_model.clearCurrentIndex()
        return QtWidgets.QLineEdit.closeEvent(self, event)

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Return) or \
           (event.key() == QtCore.Qt.Key_Enter):
               self.parent().set_selected_value()
        if event.key() == QtCore.Qt.Key_Tab:
            self.select_next_item()
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            self.parent().setFocus()
        return QtWidgets.QListView.keyPressEvent(self, event)

