from PySide6 import QtWidgets, QtCore, QtGui
from gui.project_widgets.dialogs.select_project_dialog import SelectProjectDialog

class HeaderPannel(QtWidgets.QWidget):
    """Description"""
    def __init__(self, parent=None):
        super().__init__(parent)

        # Palette
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                     QtGui.QColor("#008800"))
        self.setPalette(pal)
        self.setAutoFillBackground(True)
        # ---------------
        self.user = self.parent().user

        lay_main_hor = QtWidgets.QHBoxLayout(self)

        self.btn_sidebar = QtWidgets.QPushButton("+")
        self.btn_account = QtWidgets.QPushButton("Account")
        self.btn_project = QtWidgets.QPushButton("...")

        self.btn_sidebar.clicked.connect(self.sidebar_OnOff)
        self.btn_project.clicked.connect(self.select_project)

        lay_main_hor.addWidget(self.btn_sidebar, 0,
                               QtCore.Qt.AlignLeft)
        lay_main_hor.addWidget(self.btn_project, 0,
                               QtCore.Qt.AlignLeft)

        lay_main_hor.addWidget(self.btn_account, 0,
                               QtCore.Qt.AlignRight)

    def sidebar_OnOff(self):
        if self.parent().sidebar.isVisible():
            self.parent().sidebar.setVisible(False)
        else:
            self.parent().sidebar.set_position()
            self.parent().sidebar.setVisible(True)
            self.parent().sidebar.raise_()

    def select_project(self):
        w = SelectProjectDialog(self)
        print("before")
        print(w.size())
        print(w.parent())
#         w.setWindowModality(QtCore.Qt.ApplicationModal)
        w.exec_()
#         w.raise_()
#         w.activateWindow()
#         print(w.sizeHint())
#         print(w.pos())
        print(w.isVisible())
        print("after")