from PySide6 import QtWidgets

class AgreementTabsW(QtWidgets.QTabWidget):

    def __init__(self,
                 agreements_widget,
                 offers_widget=None,
                 parent=None):
        super().__init__(parent)

        self.addTab(agreements_widget, "Agreements")
        self.addTab(offers_widget, "Offers")
