class BaseUser:

    def __init__(self, login):
        self.id = ""
        self.login = login
        self.name = ""
        self.email = ""
        self.icon = ""

        self.colleagues = []


    def get_relationsip(self, person):
        pass

    def get_pojects(self):
        pass

    def get_shares(self, person):
        pass

    def get_standby(self):
        pass

    def get_colleagues(self, server):
#         colleagues = server.get_colleagues(self.id)
        response = server.get_users("%")
        if response[0] is not True:
            return []

        colleagues = []
        users_data = response[1]
        for person in users_data:
            user = BaseUser(person.get('login'))
            user.id = person.get('id_user')
            user.id = person.get('email')
            colleagues.append(user)
#             print("------------PERSON---------------", person)
        return colleagues
