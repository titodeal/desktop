#!/usr/bin/python
from titoshare_client.api import ApiShare
from app.api_client import Api as ApiServer
import sys


# with ApiShare(host='192.168.88.163', port=5055, timeout=None) as api_share:
#     api_share.mount_fs("/home/new_user/folder/for_other", "fed", "123",
#                  "192.168.88.163", "22")
#     api_share.umount_fs("/home/new_user/folder/for_other")
#     api_share.share_catalog("/home/new_user", "user_tst", "321")
#     pass

# with ApiServer(host='192.168.88.163', port=9090, timeout=None) as api_server:
#     for i in range(int(sys.argv[1]), int(sys.argv[2])):
# 
#         retruncode, data = api_server.add_user("User_" + str(i).zfill(2),
#                                                "123",
#                                                "trata@gamil_"
#                                                + str(i).zfill(2) + ".com")
#         print("RETURNCODE IS: ", retruncode)
#         print("DATA IS: ", data)

api_server = ApiServer(host='192.168.88.163', port=9090, timeout=None)
# api_server.set_connection()

# returncode, data = api_server.del_user("User_01")
returncode, data = api_server.add_user("User_001", "123", "trata@gamil_01")
print("RETRUN CODE IS: ", returncode)
print("DATA IS: ", data)

api_server.close_connection()

