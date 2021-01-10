# from argon2 import PasswordHasher
# 
# class UserCredential:
#     def __init__(self, login, passwd=None):
#         self.login = login
#         self.passwd = passwd
# 
#     def check_user_access(self, passwd, true_hash):
#         ph = PasswordHasher()
#         phash = ph.hash(passwd)
# 
#         is_correct = ph.verify(true_hash, passwd)
#         print("Checking passwd is: ", is_correct)
# 
# 
#     def set_user_credential(self, passwd):
#         pass
# 
# 
