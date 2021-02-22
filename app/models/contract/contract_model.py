class ContractModel:
    def __init__(self, _id,
                 agreement_id,
                 contractor_id,
                 contractor,
                 project_id,
                 project,
                 accepted,
                 documents=[],
                 departments="",
                 specialty="",
                 role="",
                 date=""):

        self.id = _id
        self.agreement_id = agreement_id
        self.contractor_id = contractor_id
        self.contractor = contractor
        self.project_id = project_id
        self.project = project
        self.accepted = accepted
        self.documents = documents
        self.departments = departments
        self.specialty = specialty
        self.role = role
        self.date = date

    @staticmethod
    def get_user_contracts(server, user_id):
        respone = server.get_user_contracts(user_id)
        if not respone[0]:
            return []

        contracts = []
        for cntr in respone[1]:
            contract = ContractModel(cntr["contract_id"],
                                     cntr["agreement_id"],
                                     cntr["contractor_id"],
                                     cntr["contractor"],
                                     cntr["project_id"],
                                     cntr["project"],
                                     cntr["accepted"],
                                     cntr["documents"],
                                     cntr["departments"],
                                     cntr["specialty"],
                                     cntr["role"],
                                     cntr["date"])
            contracts.append(contract)
        return contracts

