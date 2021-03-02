from PySide6 import QtWidgets, QtCore


class FirstRowDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if index.row() != 0:
            return QtWidgets.QStyledItemDelegate. \
                   paint(self, painter, option, index)
        if not self.parent().isPersistentEditorOpen(index):
            self.parent().openPersistentEditor(index)

    def createEditor(self, parent, options, index):
        if index.row() != 0:
            return QtWidgets.QStyledItemDelegate. \
                   createEditor(self, parent, options, index)
        editor = FirstRowWidget(parent)
#         editor.setAutoFillBackground(True)
        index = index.column()
        editor.btn_menu.clicked.connect(lambda x=index: print(index))
        return editor

    def setEditorData(self, editor, index):
        return QtWidgets.QStyledItemDelegate.setEditorData(self, editor, index)

    def updateEditorGeometry(self, editor, options, index):
        if index.row() != 0:
            return QtWidgets.QStyledItemDelegate. \
                   updateEditorGeometry(self, editor, options, index)
        editor.setGeometry(options.rect)

    def setModelData(self, editor, model, index):
        return QtWidgets.QStyledItemDelegate. \
               setModelData(self, editor, model, index)


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

