import os
import sys

external_path = os.path.abspath("..")
sys.path.append(external_path)

from tito_sockets.socket_client import SocketClient


class Api(SocketClient):

    def __init__(self, host, port, timeout=None):
        super(Api, self).__init__(host=host, port=port, timeout=timeout)
        self.set_connection()

    def create_credentials(self, login, passwd, email):
        method_name = "create_credentials"
        args = [f"{login}", f"{passwd}", f"{email}"]
        response = self.send_request(method_name, args)
        return response

    def get_credentials(self, login, passwd):
        method_name = "get_credentials"
        args = [f"{login}", f"{passwd}"]
        response = self.send_request(method_name, args)
        return response

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
# 
#     def get_colleagues(self, login):
#         method_name = "get_colleagues"
#         args = [f"{login}"]
#         response = self.send_request(method_name, args)
#         return response

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

#     def get_user_offers(self, user_id):
#         method_name = "get_user_offers"
#         args = [f"{user_id}"]
#         response = self.send_request(method_name, args)
#         return response
# 
#     def get_user_contractors(self, user_id):
#         method_name = "get_user_contractors"
#         args = [f"{user_id}"]
#         response = self.send_request(method_name, args)
#         return response

#     def uadd_user(self, mnt_folder):
#         method_name = "uadd_user"
#         args = [f"{mnt_folder}"]
#         self.send_request(method_name, args)
# 
#     def share_catalog(self, catalog, user, passwd):
#         method_name = "share_catalog"
#         args = [f"{catalog}", f"{user}", f"{passwd}"]
#         self.send_request(method_name, args)

    def send_request(self, method_name, args):
        """ Response raw data looks like:
        {returncode: 0|1:int, type: answer|tb_data:str,
        data: raw_data:list, columns: items:list}
        """
        message = {"method": f"{method_name}", "args": args}
        self.send_data(message)
        response = self.recv_messages()
        print(f"=> Method process: {method_name} => Response is: {response}")
        return self.__handle_response(response)

    def __handle_response(self, response):
        """Handles response data """

        returncode = response['returncode']
        response_data = response['data']
        type_ = response['type']

        if returncode != 0:
            print("!=> Error occured: {}".format(response_data))
            return False, response_data

        if type_ == "answer":
            print("=> ", response_data)
            return True, response_data

        if type_ == "tb_data":
            data = []
            for row in response_data:
                row_data = {}
                for idx, column in enumerate(response['columns']):
                    row_data[column] = row[idx]
                data.append(row_data)
            return True, data

        else:
            msg = "!=> Unknown  response type"
            print(msg)
            return False, msg
