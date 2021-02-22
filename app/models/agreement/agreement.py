# /////////////// DEPRICATED /////////////// 
class Agreement:
    def __init__(self):

        self.id = None
        self.owner_id = ""
        self.owner_login = ""
        self.contractor_id = None
        self.contractor_login = ""
        self.conditions = ""
        self.accepted = None
        self.expiration = ""
        self.type = ""


class Agreement_:
    def __init__(self, user_id, id_, owner_id, owner_login,
                 contractor_id, contractor_login, accepted,
                 conditions="", expiration=""):
        # the login can be both owner or contractor depending on the user
        self.login = ""

        self.id = id_
        self.owner_id = owner_id
        self.owner_login = owner_login
        self.contractor_id = contractor_id
        self.contractor_login = contractor_login

        self.accepted = "Accepted" if accepted else "Expected"
        self.conditions = conditions
        self.expiration = expiration

        self.type = ""
        self._set_contract_type(user_id)

    def _set_contract_type(self, user_id):
        if user_id == self.owner_id:
            self.login = self.contractor_login
            self.type = "contractor"
        elif user_id == self.contractor_id:
            self.login = self.owner_login
            self.type = "employer"
        else:
            print("!=> Undefind user relatively agreement: "
                  f"user_id: {user_id}"
                  f"agreement_id: {self.id}")
            self.type = ""

    @staticmethod
    def get_user_agreements(server, user_id):
        response = server.get_user_agreements(user_id)
        if not response[0]:
            return [], []

        agreements = []
        for agree in response[1]:
            agreement = Agreement_(user_id,
                                   agree["agreement_id"],
                                   agree["owner_id"],
                                   agree["owner_login"],
                                   agree["contractor_id"],
                                   agree["contractor_login"],
                                   agree["accepted"],
                                   agree["conditions"],
                                   agree["expiration"])
            agreements.append(agreement)

        return agreements
