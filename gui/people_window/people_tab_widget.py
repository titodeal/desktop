from PySide6 import QtWidgets

class PeopleTabWidget(QtWidgets.QTabWidget):

    def __init__(self,
                 colleagues_widget,
                 standby_widget=None,
                 other_widget=None,
                 parent=None):

        super().__init__(parent)

        self.addTab(colleagues_widget, "Colleagues")
        self.addTab(standby_widget, "Stand by")
        self.addTab(other_widget, "Other")
