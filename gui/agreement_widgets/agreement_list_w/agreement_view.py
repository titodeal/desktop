from PySide6 import QtCore, QtWidgets

from .agreement_model import AgreementModel


class AgreementView(QtWidgets.QTableView):

    def __init__(self, agreements, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.setModel(AgreementModel(agreements))
        self.doubleClicked.connect(self.add_user_tab)

    def selectionChanged(self, item, prev_item):
        if not self.parent.agreement_prop_section:
            return
        self.parent.agreement_prop_section.replace_current_agreement()
# 

    def add_user_tab(self):
        self.parent.userprop_tab_widget.add_user_tab()
