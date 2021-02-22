from app.models.agreement import utils as agreement_utils
from app.models.project.project_model import ProjectModel


class BaseUser:
    __server = None

    def __init__(self, login, server=None):
        self.id = ""
        self.login = login
        self.first_name = ""
        self.last_name = ""
        self.phone = ""
        self.email = ""
        self.icon = ""

        self.projects = []
        self.current_project = None
        self.offers = []
        self.contractors = []
        self.employers = []
        self.standby_offers = []

        if server:
            BaseUser.__server = server
            self.update_user_data()

    def get_server(self):
        return self.__server

    def update_user_data(self):
        response = self.__server.get_users(self.login)
        if not response[0]:
            raise ValueError(f"!=> The user: '{self.login}' not found in database")
        user_data = response[1][0]
        self.id = user_data['user_id']
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.phone = user_data['phone']
        self.email = user_data['email']
        self.projects = self.get_user_projects()
        if self.projects:
            self.set_current_project(self.projects[0])

    def get_user_projects(self):
        return ProjectModel.get_user_projects(self.get_server(), self.id)

    def set_current_project(self, project):
        self.current_project = project

    def send_offer(self, contractor_id):
        return_status, msg = self.__server.send_offer(self.id, contractor_id)
        return return_status

    #/////////////// DEPRICATED //////////////////////
    def get_agreements(self):
        response = self.__server.get_user_agreements(self.id)
        if not response[0]:
            return [], []

#         print(response[1])
        agreements = []
        offers = []
        for agree in response[1]:
            if agree.get('accepted'):
                agreements.append(agree)
            else:
                offers.append(agree)

        agreements = agreement_utils.from_dicts_to_agreements(self.id, agreements)
        offers = agreement_utils.from_dicts_to_agreements(self.id, offers)
        return agreements, offers
#         print("======USER AGREEMENTS IS =================", response)
#         print("======USER AGREEMENTS IS =================")

    def get_relationsip(self, person):
        pass

    def get_pojects(self):
        pass

    def get_shares(self, person):
        pass

    def get_standby(self):
        pass

    def get_contractors(self):
        response = self.__server.get_user_contractors(self.id)
        if response[0] is not True:
            return []
        return self._from_dicts_to_users(response[1])
#         return response[1]


    def get_colleagues(self):
#         colleagues = server.get_colleagues(self.id)
        response = self.__server.get_users("%")
        if response[0] is not True:
            return []

        return self._from_dicts_to_users(response[1])
#         colleagues = []
#         users_data = response[1]
#         for person in users_data:
#             user = BaseUser(person.get('login'))
#             user.id = person.get('id_user')
#             user.email = person.get('email')
#             colleagues.append(user)
# #             print("------------PERSON---------------", person)
#         return colleagues

    def get_all_users(self):
        response = self.__server.get_users("%")
        if response[0] is not True:
            return []

        return self._from_dicts_to_users(response[1])
#         users = []
#         users_data = response[1]
#         for person in users_data:
#             user = BaseUser(person['login'])
#             user.id = person['user_id']
#             user.first_name = person['first_name']
#             user.last_name = person['last_name']
#             user.phone = person['phone']
#             user.email = person['email']
#             users.append(user)
#         return users

    def _from_dicts_to_users(self, dicts):
        users = []
        for d in dicts:
            user = BaseUser(d['login'])
            user.id = d['user_id']
            user.first_name = d['first_name']
            user.last_name = d['last_name']
            user.phone = d['phone']
            user.email = d['email']
            users.append(user)
        return users


