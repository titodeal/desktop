from PySide6 import QtWidgets, QtCore

from app.models.contract.contract_model import ContractModel
from app.models.agreement.agreement import Agreement_
from gui.agreement_widgets.dialogs.select_agreement_dialog import AgreementsSelectDialog
# from gui.agreement_widgets.agreement_table.agreement_table_w import AgreementsTable

class ContractProperties(QtWidgets.QWidget):
    new_contract_signal = QtCore.Signal(ContractModel, name="new_contract_signal")

    def __init__(self, parent, project):
        super().__init__(parent)

        self.user = self.parent().user
        self.server = self.user.get_server()

        self.project = project
        self.agreement = None
#         self.project = "None" if project is None else project
#         self.project_id = 0000 if project is None else project.id

        self.resize(500, 500)

        # --------------- Layouts --------------- 
        self.lay_main_ver = QtWidgets.QVBoxLayout(self)
        self.lay_fields_form = QtWidgets.QFormLayout()

        # --------------- Widgets --------------- 
        self.lb_contract_id = QtWidgets.QLabel("None")
        self.lb_project_name = QtWidgets.QLabel(self.project.name)
        self.fl_agreement_w = self._get_agreement_field()

        self.lb_department = QtWidgets.QLabel("Some Department")
        self.lb_speciality = QtWidgets.QLabel("Some Speciality")
        self.lb_role = QtWidgets.QLabel("Some Role")
        self.lb_status = QtWidgets.QLabel("Some Stauts")

        self.btn_save = QtWidgets.QPushButton("Save")
        self.btn_send = QtWidgets.QPushButton("Send")
        if project is None:
            self.btn_save.setEnabled(False)
            self.btn_send.setEnabled(False)
        self.btn_send.clicked.connect(self.send_contract)
        self.lay_btn_hor = QtWidgets.QHBoxLayout()
        self.lay_btn_hor.addWidget(self.btn_save)
        self.lay_btn_hor.addWidget(self.btn_send)


        # --------------- Layouts setup --------------- 
        self.lay_fields_form.addRow("Contract ID:",  self.lb_contract_id)
        self.lay_fields_form.addRow("Project:",  self.lb_project_name)
        self.lay_fields_form.addRow("Agreement:",  self.fl_agreement_w)
        self.lay_fields_form.addRow("Department:",  self.lb_department)
        self.lay_fields_form.addRow("Speciality:",  self.lb_speciality)
        self.lay_fields_form.addRow("Role:",  self.lb_role)
        self.lay_fields_form.addRow("Status:",  self.lb_status)

        self.lay_main_ver.addLayout(self.lay_fields_form)
        self.lay_main_ver.addLayout(self.lay_btn_hor)

#     def add_field(label, type_="QtWidgets.QLabel", btn_w=None):
#         pass

    def _get_agreement_field(self):
        fl_agreement_w = QtWidgets.QWidget()
        fl_agreement_w.lb_label = QtWidgets.QLabel("")

        fl_agreement_w.btn_edit = QtWidgets.QPushButton(">")
        fl_agreement_w.btn_edit.setFlat(True)
        fl_agreement_w.btn_edit.setFixedWidth(20)
        fl_agreement_w.btn_edit.clicked.connect(self.select_agreement_dialog)

        lay_hor = QtWidgets.QHBoxLayout(fl_agreement_w)
        lay_hor.setContentsMargins(0, 0, 0, 0)
        lay_hor.setSpacing(0)

        lay_hor.addWidget(fl_agreement_w.lb_label)
        lay_hor.addWidget(fl_agreement_w.btn_edit, 1, QtCore.Qt.AlignLeft)
        return fl_agreement_w

    def select_agreement_dialog(self):
        agreements = Agreement_.get_user_agreements(self.server, self.user.id)
        agreements_select_dialog = AgreementsSelectDialog(self, objects=agreements)

        result = agreements_select_dialog.exec_()
        if not result == QtWidgets.QDialog.Accepted:
            return
        self.agreement = agreements_select_dialog.current_object
        if self.agreement:
            self.fl_agreement_w.lb_label.setText(self.agreement.login)
#             self.agreement_id = agreement_obj.id

    def send_contract(self):
        response = self.server.send_contract(self.project.id, self.agreement.id)
        if not response[0]:
            print("!=> Sending contract faild: ", response[1])
            return
        data = response[1]
        if not data:
            return
        contract_dbdata = data[0]
        print("Contrat sent successfull!: ", data)
        contract_data = {"_id": contract_dbdata["contract_id"],
                          "agreement_id": self.agreement.id,
                          "contractor_id": self.agreement.owner_id,
                          "contractor": self.agreement.login,
                          "project_id": self.project.id,
                          "project": self.project.name,
                          "accepted": False,
                          "documents": contract_dbdata["documents"],
                          "departments": contract_dbdata["departments"],
                          "specialty": contract_dbdata["specialty"],
                          "role": contract_dbdata["role"],
                          "date": contract_dbdata["date"]}
        new_contract = ContractModel(**contract_data)
        self.new_contract_signal.emit(new_contract)
#         print(new_contract)
