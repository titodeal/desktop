#!/usr/bin/python
from titoshare_client.api import Api


with Api(host='192.168.88.163', port=5055, timeout=None) as api:
    api.mount_fs("/home/new_user/folder/for_other", "fed", "123",
                 "192.168.88.163", "22")
    api.umount_fs("/home/new_user/folder/for_other")
#     api.share_catalog("/home/new_user", "user_tst", "321")
