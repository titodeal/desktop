import os
import sys

external_path = os.path.abspath("..")
sys.path.append(external_path)

from tito_sockets.socket_client import SocketClient


class Api(SocketClient):

    def __init__(self, host, port, timeout=None):
        super(Api, self).__init__(host=host, port=port, timeout=timeout)
        self.set_connection()

    def add_user(self, username, passwd, email):
        method_name = "add_user"
        args = [f"{username}", f"{passwd}", f"{email}"]
        response = self.send_request(method_name, args)
        return response

    def del_user(self, username):
        method_name = "del_user"
        args = [f"{username}"]
        response = self.send_request(method_name, args)
        return response

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
        message = {"method": f"{method_name}", "args": args}
        self.send_data(message)
        response = self.recv_messages()
        print(f"=> Method process: {method_name} => Response is: {response}")
        return response
