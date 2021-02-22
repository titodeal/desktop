from PySide6 import QtWidgets
from ..agreement_table.agreement_table_w import AgreementsTable


class AgreementsSelectDialog(QtWidgets.QDialog):
    def __init__(self, parent, objects=[]):
        super().__init__(parent)

        self.current_object = None

        self.lay_main_ver = QtWidgets.QVBoxLayout(self)
        self.lay_main_ver.setContentsMargins(0, 0, 0, 0)

        self.table = AgreementsTable(parent, objects)
        self.table.set_items_checkable(True)

        self.btn_select = QtWidgets.QPushButton("Select")
        self.btn_select.setFlat(True)
        self.btn_cancel = QtWidgets.QPushButton("Cancel")
        self.btn_cancel.setFlat(True)


        self.buttons = QtWidgets.QDialogButtonBox(self)
        self.buttons.addButton(self.btn_select, QtWidgets.QDialogButtonBox.AcceptRole)
        self.buttons.addButton(self.btn_cancel, QtWidgets.QDialogButtonBox.RejectRole)
        self.buttons.accepted.connect(self.select)
        self.buttons.rejected.connect(self.reject)

        self.lay_main_ver.addWidget(self.table)
        self.lay_main_ver.addWidget(self.buttons)

    def select(self):
        self.current_object = self.table.table.get_current_object()
        self.accept()

#     def reject(self):
#         self.reject()
#         print("reject")
