from PySide6 import QtWidgets, QtCore
from gui.utils import window_managment
from .sidelist_widget.sidelist_widget import SidelistWidget

from .roots_settings.root_main_w import RootsMainWidget


class SettingsMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Settings")
        self.setWindowFlags(QtCore.Qt.Window)
        self.resize(300, 300)
        window_managment.adjust_by_screen(self)

        self.user =  self.parent().user

        # --------------- Layouts ---------------
        self.lay_main_hor = QtWidgets.QHBoxLayout(self)
        self.lay_main_hor.setContentsMargins(0, 0, 0, 0)
        self.lay_main_hor.setSpacing(0)
        self.lay_stack = QtWidgets.QStackedLayout()
        self.lay_stack.setSpacing(0)
#         self.lay_stack.setContentsMargins(0, 0, 0, 0)

        # -------------- All setting widgets  ------------
        self.roots_widget = RootsMainWidget(self, self.user)
        self.sharing_widget = SharingSettings(self)

        setting_widgets = [self.roots_widget,
                           self.sharing_widget]

        # -------------- Sidelist Widget ------------
        self.sidelist_widget = SidelistWidget(self, setting_widgets)

        # -------------- Signals  ------------
        self.sidelist_widget.selection_model.currentChanged.connect(self.change_widget)

        # -------------- Layouts setup  ------------
        for w in setting_widgets:
            self.lay_stack.addWidget(w)
        self.lay_main_hor.addWidget(self.sidelist_widget)
        self.lay_main_hor.addLayout(self.lay_stack)

    def change_widget(self, index, pre_index):
        self.lay_stack.setCurrentIndex(index.row())


# class RootsWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
# 
#         self.name = "Roots for All Remote User"
#         self.lay_main_ver = QtWidgets.QVBoxLayout(self)
#         self.lay_main_ver.setContentsMargins(0, 0, 0, 0)
#         self.lay_main_ver.setSpacing(0)
#         self.tst_label = QtWidgets.QLabel("TEST ROOTS WIDGET")
#         self.lay_main_ver.addWidget(self.tst_label)


class SharingSettings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.name = "Sharing Remote User"
        self.lay_main_ver = QtWidgets.QVBoxLayout(self)
        self.tst_label = QtWidgets.QLabel("TEST Sharing WIDGET")
        self.lay_main_ver.addWidget(self.tst_label)
