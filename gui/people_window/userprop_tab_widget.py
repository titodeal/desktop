from PySide6 import QtWidgets
from gui.user_widget import user_properties


class UserPropTabWidget(QtWidgets.QTabWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.add_user_tab()
        self.setTabsClosable(True)

        self.tabCloseRequested.connect(self.close_tab)

    def replace_current_user(self):
        user = self.get_current_user()
        if not user:
            return

        w = user_properties.UserProperties(user)

        currIndex = self.currentIndex()
        self.removeTab(currIndex)
        idx = self.insertTab(currIndex, w, user.login)
        self.setCurrentIndex(idx)

    def add_user_tab(self, user=None):
        if user is None:
            user = self.get_current_user()
            if not user:
                return
        w = user_properties.UserProperties(user)
        currIndex = self.currentIndex()
        self.insertTab(currIndex, w, user.login)
        self.setCurrentIndex(currIndex)
#         self.addTab(w, user.login)

    def get_current_user(self):
        people_widget = self.parent().people_tab_widget.currentWidget()
        currRow = people_widget.currentIndex().row()
        if currRow == -1:
            return
        user = people_widget.model().get_user_instance(currRow)
        return user

    def close_tab(self):
        self.currentWidget().close()
        self.removeTab(self.currentIndex())

