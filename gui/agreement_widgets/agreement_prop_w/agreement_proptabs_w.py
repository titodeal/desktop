from PySide6 import QtWidgets
from . import agreement_properties


class AgreementPropTabW(QtWidgets.QTabWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.add_agreement_tab()
        self.setTabsClosable(True)

        self.tabCloseRequested.connect(self.close_tab)

    def replace_current_agreement(self):
        agreement = self.get_current_agreement()
        if not agreement:
            return

        w = agreement_properties.AgreementProperties(agreement, self.parent().user, parent=self)

        currIndex = self.currentIndex()
        self.removeTab(currIndex)
        idx = self.insertTab(currIndex, w, str(agreement.id))
        self.setCurrentIndex(idx)

    def add_agreement_tab(self, agreement=None):
        if agreement is None:
            agreement = self.get_current_agreement()
            if not agreement:
                return
        w = user_properties.UserProperties(user, self.parent().user, parent=self)
        currIndex = self.currentIndex()
        self.insertTab(currIndex, w, user.login)
        self.setCurrentIndex(currIndex)
#         self.addTab(w, user.login)

    def get_current_agreement(self):
        agreement_widget = self.parent().agreement_list_section.currentWidget()
        currRow = agreement_widget.currentIndex().row()
        if currRow == -1:
            return
        agreement = agreement_widget.model().get_agreement_instance(currRow)
        return agreement

    def close_tab(self):
        self.currentWidget().close()
        self.removeTab(self.currentIndex())

