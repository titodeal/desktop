
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
