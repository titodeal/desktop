from PySide6 import QtWidgets, QtCore, QtGui
# from gui.custom_widgets.table_filters_widget import table_filters_w
from app.models.contract.contract_model import ContractModel
from .contracts_table_w import ContractsTableWidget
from .contract_properties import ContractProperties


# class ContractsMainWidget(QtWidgets.QWidget):
class ContractsMainWidget(QtWidgets.QSplitter):
    def __init__(self, parent, user, headers=[], contracts=[]):
        super().__init__(parent)

        self.user = user
        self.server = user.get_server()

        self.contracts = contracts
#         self.headers = ["contract_id", "project_name", "agreement_id", "user"]

        self.lay_main_hor = QtWidgets.QHBoxLayout(self)
        self.lay_main_hor.setContentsMargins(0, 0, 0, 0)

        self._setup_table()
#         self._other_widget = QtWidgets.QWidget(self)
#         self._other_widget.setBaseSize(200, 200)

        self.addWidget(self.table)
#         self.addWidget(self._other_widget)
#         self.setCollapsible(0, False)

        self.properties_w = ContractProperties(self, user.current_project)
        self.properties_w.new_contract_signal.connect(self.new_contract_created)
        self.addWidget(self.properties_w)
#         self.properties_w.show()
#         self.properties_w.raise_()
#         self.lay_main_hor.addWidget(self.table)

    def _setup_table(self):
        contracts = ContractModel.get_user_contracts(self.server, self.user.id)
        self.table = ContractsTableWidget(self, contracts)
        self.table.table_view.setItemDelegateForColumn(0, FirstRowDelegate(self.table.table_view))

        self.table.insert_rows([FirstRow(self.table.headers)], 0)
        self.table.table_view.setSpan(0, 0, 1, 4)
#         self.table.append_rows([FirstRow(self.table.headers)])
#         self.table.append_rows([FirstRow(self.table.headers)])
#         self.table.set_items_flags(QtCore.Qt.ItemIsEnabled \
#                       | QtCore.Qt.ItemIsEditable \
#                       | QtCore.Qt.ItemIsSelectable \
#                       | QtCore.Qt.ItemNeverHasChildren)

    def new_contract_created(self, contract):
        self.table.insert_rows([contract], 1)
#         self.table.update_table_data()

    def update_table_data(self, objects):
        pass
        #get new server data
        #insert the first row to objects list
        #set span for first row
        #update table model


class FirstRow:
    def __init__(self, headers):
        for h in headers:
            setattr(self, h, None)

class FirstRowDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if index.row() != 0:
            return QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
        if not self.parent().isPersistentEditorOpen(index):
            self.parent().openPersistentEditor(index)

    def createEditor(self, parent, options, index):
        if index.row() != 0:
            return QtWidgets.QStyledItemDelegate.createEditor(self, parent, options, index)
        editor = FirstRowWidget(parent)
#         editor.setAutoFillBackground(True)
        index = index.column()
        editor.btn_menu.clicked.connect(lambda x=index: print(index))
        return editor

    def setEditorData(self, editor, index):
        return QtWidgets.QStyledItemDelegate.setEditorData(self, editor, index)

    def updateEditorGeometry(self, editor, options, index):
        if index.row() != 0:
            return QtWidgets.QStyledItemDelegate.updateEditorGeometry(self, editor, options, index)
        editor.setGeometry(options.rect)

    def setModelData(self, editor, model, index):
        return QtWidgets.QStyledItemDelegate.setModelData(self, editor, model, index)


class FirstRowWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.lay_main_hor = QtWidgets.QHBoxLayout(self)
        self.lay_main_hor.setContentsMargins(0, 0, 0, 0)
        self.lay_main_hor.setSpacing(0)
        self.lb_new = QtWidgets.QLabel("  -- NEW")

        self.btn_menu = QtWidgets.QPushButton(">")
        self.btn_menu.setFixedWidth(15)
        self.btn_menu.setFlat(True)

        self.lay_main_hor.addWidget(self.lb_new, 0, QtCore.Qt.AlignLeft)
        self.lay_main_hor.addWidget(self.btn_menu, 0, QtCore.Qt.AlignLeft)
        self.lay_main_hor.addStretch()

