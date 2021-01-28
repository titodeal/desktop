from PySide6 import QtCore


class AgreementModel(QtCore.QAbstractTableModel):

    def __init__(self, agreements=[], parent=None):
        super().__init__(parent)

        self.agreements = agreements
        self.columns = ["Login", "Type", "Expiration"]

    def rowCount(self, parent):
        return len(self.agreements)

    def columnCount(self, parent):
        return len(self.columns)

    def data(self, index, role):
        # --------- Display role -------------
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                type_ = self.agreements[index.row()].type
                if type_ == "employer":
                    return self.agreements[index.row()].contractor_login
                else:
                    return self.agreements[index.row()].owner_login
            if index.column() == 1:
                return self.agreements[index.row()].type
            if index.column() == 2:
                return self.agreements[index.row()].expiration
        # -----------------------------------

    def setData(self, index, value, role):
        pass

#     def insertRows(self, row, count, values=None, parent=QtCore.QModelIndex()):
    def insertRows(self, row, agreements_data, parent=QtCore.QModelIndex()):
        count = len(users_data)
        self.beginInsertRows(parent, row, row+count-1)
        self.users[row:row] = agreements_data
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QtCore.QModelIndex()):
        count=2
        self.beginRemoveRows(parent, row, row+count-1)
        self.agreements[row:row+count] = []
        self.endRemoveRows()
        return True

    def get_agreement_instance(self, row):
        return self.agreements[row]

    def reset_model(self, users_data):
        self.endResetModel()
