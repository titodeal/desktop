from PySide6 import QtCore
# from app.models.user.main_user import MainUser
# from app.models.user.base_user import BaseUser


class PeopleTableModel(QtCore.QAbstractTableModel):

    def __init__(self, users=[], parent=None):
        super().__init__(parent)

        self.users = users
        self.columns = ["Login"]

    def rowCount(self, parent):
        return len(self.users)

    def columnCount(self, parent):
        return len(self.columns)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.users[index.row()].login

    def setData(self, index, value, role):
        pass

#     def insertRows(self, row, count, values=None, parent=QtCore.QModelIndex()):
    def insertRows(self, row, users_data, parent=QtCore.QModelIndex()):
        count = len(users_data)
        self.beginInsertRows(parent, row, row+count-1)
        self.users[row:row] = users_data
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QtCore.QModelIndex()):
        count=2
        self.beginRemoveRows(parent, row, row+count-1)
        self.users[row:row+count] = []
        self.endRemoveRows()
        return True

    def get_user_instance(self, row):
        return self.users[row]

    def reset_model(self, users_data):
        self.endResetModel()
