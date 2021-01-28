from PySide6 import QtWidgets

from .agreement_view import AgreementView
from .agreement_tabs_w import AgreementTabsW


class collectingAgreementsW(QtWidgets.QtWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lay_main_vert = QtWidgets.QVBoxLayout()

        agreemetns=[]
        self.agreements_tabs = AgreementTabsW(agreements)
        offers = []
        self.agreements_
