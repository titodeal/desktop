from PySide6 import QtWidgets, QtCore, QtGui


class SideBar(QtWidgets.QToolBar):
    """Description"""
    def __init__(self, name="", parent=None):
        super().__init__(name, parent)

        self.setOrientation(QtCore.Qt.Vertical)

        # -------- Buttons -----------------
        self.btn_group = QtWidgets.QButtonGroup()
        self.btn_home = self.add_button("Home",
                lambda x: self.btn_action(self.btn_home.text()))

        self.btn_agreements = self.add_button("Agreements",
                lambda x: self.btn_action(self.btn_agreements.text()))

        self.btn_people = self.add_button("People",
                lambda x: self.btn_action(self.btn_people.text()))

        self.btn_projects = self.add_button("Projects",
                lambda x: self.btn_action(self.btn_projects.text()))
        #---------------------------------

        self.addWidget(self.btn_home)
        self.addWidget(self.btn_agreements)
        self.addWidget(self.btn_people)
        self.addWidget(self.btn_projects)

        self.addSeparator()
        self.setAutoFillBackground(True)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.btn_group.buttonClicked.connect(self.btn_grp_click)

        self.set_visibility()

    def add_button(self, text, action, icon=None):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(action)
        self.btn_group.addButton(button, len(self.btn_group.buttons()))
        return button

    def btn_grp_click(self, btn):
        btn.setDown(True)

    def btn_action(self, btn):
        if btn == "Agreements":
            self.parent().lay_main_stacked.setCurrentIndex(0)
        if btn == "People":
            self.parent().lay_main_stacked.setCurrentIndex(1)
        self.raise_()
        print(btn)

    def set_visibility(self):
        self.setVisible(False)

    def set_position(self, parent_size=None):
        if not parent_size:
            parent_size = self.parent().size()
        header_pannel_size = self.parent().header_pannel.sizeHint()

        upper_offset = header_pannel_size.height()
        height = parent_size.height() - upper_offset
        width = parent_size.width() * .25

        self.setGeometry(0, upper_offset, width, height)
#         self.raise_()


# class MyMenu(QtWidgets.QMenu):
#     def __init__(self, parent=None):
#         super().__init__(parent)
# 
#     def event(self, event):
# 
#         parent = self.parent()
#         parent.activateWindow()
#         parent.raise_()
#         parent.btn.setFocus()
#         parent.btn.activateWindow()
# #         parent.btn2.activateWindow()
# #         print(self.parent().focusWidget())
# #         print(parent)
#         return QtWidgets.QWidget.event(self, event)
# 
# 
# class MenuButton(QtWidgets.QPushButton):
#     def __init__(self, parent=None):
#         super().__init__(parent)
# 
#     def event(self, event):
#         self.blockSignals(True)
#         if event.type() == QtCore.QEvent.Enter:
#             print("SHOW")
# #             self.menu().setWindowFlags(QtCore.Qt.Dialog)
#             print(self.menu().windowType())
# #             self.parent().menu.show()
# #             self.menu().setFocusPolicy(QtCore.Qt.NoFocus)
#             self.showMenu()
#             self.menu().hide()
# 
#         if event.type() == QtCore.QEvent.Leave:
#             print("HIDE")
#             self.menu().hide()
#         return QtWidgets.QWidget.event(self, event)
