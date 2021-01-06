from app import api_client


HOST = "192.168.88.163"
PORT = 9090


class UserSereverCore:
    def __init__(self, username, passwd):
        self.api_server = api_client.Api(HOST, PORT)
#         self.get_credentials(username, passwd)

    def get_credentials(self, username, passwd):
        returncode, data = self.api_server.get_credentials(username, passwd)
        if returncode != 0:
            return False

        return True

#         self.username = username
# 
#         self.ture_hash = None
#         self.email = None
#         self.phone = None
# 
#         self.__get_user_data(passwd)

#     def __get_user_data(self, passw):
#         exists = True
#         if not exists:
#             raise ValueError
# 
#         self.ture_hash = "lsfjslfksf"
#         self.email = "tst@urk.net"
#         self.phone  "3803455455"
#         return True
# 
#     def __
