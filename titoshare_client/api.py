import os
import sys

external_path = os.path.abspath("..")
print(external_path)
sys.path.append(external_path)

from tito_sockets.socket_client import SocketClient


class ApiShare(SocketClient):

    def __init__(self, host, port, timeout=None):
        super(ApiShare, self).__init__(host=host, port=port, timeout=timeout)
        self.set_connection()

    def mount_fs(self, mnt_folder, user, passwd, ip, port):
        method_name = "mount_fs"
        args = [f"{mnt_folder}", f"{user}", f"{passwd}", f"{ip}", f"{port}"]
        self.send_request(method_name, args)

    def umount_fs(self, mnt_folder):
        method_name = "umount_fs"
        args = [f"{mnt_folder}"]
        self.send_request(method_name, args)

    def share_catalog(self, catalog, user, passwd):
        method_name = "share_catalog"
        args = [f"{catalog}", f"{user}", f"{passwd}"]
        self.send_request(method_name, args)

    def send_request(self, method_name, args):
        message = {"method": f"{method_name}", "args": args}
        self.send_data(message)
        response = self.recv_messages()
        print(f"=> Method process: {method_name} => Response is: {response}")
