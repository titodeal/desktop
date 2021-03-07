import os
import sys
external_path = os.path.abspath("..")
sys.path.append(external_path)

from tito_sockets.socket_client import SocketClient


class TiToshClient(SocketClient):
    def __init__(self, host, port, timeout=None):
        super(TiToshClient, self).__init__(host=host, port=port, timeout=timeout)

    def _send_request(self, method_name, args):
        message = {"method": f"{method_name}", "args": args}
        self.send_data(message)
        response = self.recv_messages()
        print(f"=> Method process: '{method_name}' => Response is {response}")
        return response

def mount_fs(host, port, user, passwd, root_folder):
    conn = TiToshClient(host, port)
    conn.set_connection()
    method_name = "get_credentials"
    args = [f"{user}", f"{passwd}"]
    conn._send_request(method_name, args)

    method_name = "mount_fs"
    args = [f"{root_folder}", f"{user}", f"{passwd}"]
    conn._send_request(method_name, args)
    conn.close_connection()

def check_storage_folder(host, port, user, passwd, root_folder):
    conn = TiToshClient(host, port)
    conn.set_connection()
    method_name = "get_credentials"
    args = [f"{user}", f"{passwd}"]
    conn._send_request(method_name, args)

    method_name = "check_storage_folder"
    args = [f"{root_folder}", f"{user}"]
    response = conn._send_request(method_name, args)
    conn.close_connection()
    return response

