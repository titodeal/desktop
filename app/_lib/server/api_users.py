
class ApiUsers:
    def get_users(self, login):
        method_name = "get_users"
        args = [f"{login}"]
        response = self.send_request(method_name, args)
        return response

    def del_user(self, login):
        method_name = "del_user"
        args = [f"{login}"]
        response = self.send_request(method_name, args)
        return response

    def get_user_agreements(self, user_id):
        method_name = "get_user_agreements"
        args = [f"{user_id}"]
        response = self.send_request(method_name, args)
        return response

    def send_offer(self, owner_id, contractor_id):
        method_name = "send_offer"
        args = [f"{owner_id}", f"{contractor_id}"]
        response = self.send_request(method_name, args)
        return response

    def accept_agreement(self, agreement_id):
        method_name = "accept_agreement"
        args = [f"{agreement_id}"]
        response = self.send_request(method_name, args)
        return response

    def send_contract(self, project_id, agreement_id):
        method_name = "send_contract"
        args = [f"{project_id}", f"{agreement_id}"]
        response = self.send_request(method_name, args)
        return response

    def get_user_contracts(self, user_id):
        method_name = "get_user_contracts"
        args = [f"{user_id}"]
        response = self.send_request(method_name, args)
        return response

    def create_user_root(self, user_id, root_folder, sharing=False):
        method_name = "create_user_root"
        args = [f"{user_id}", f"{root_folder}", f"{sharing}"]
        response = self.send_request(method_name, args)
        return response

    def get_user_roots(self, user_id):
        method_name = "get_user_roots"
        args = [f"{user_id}"]
        response = self.send_request(method_name, args)
        return response
