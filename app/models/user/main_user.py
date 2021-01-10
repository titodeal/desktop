from .base_user import BaseUser

class MainUser(BaseUser):
    __server = None

    def __init__(self, server, login):
        super().__init__(login)
        MainUser.__server = server

        self.update_user_data()

    def get_user_server(self):
        return self.__server

    def update_user_data(self):
        response = self.__server.get_users(self.login)
        if not response[0]:
            raise ValueError(f"!=> The user: '{self.login}' not found in database")

        user_data = response[1][0]
        self.id = user_data.get('id_user')
        self.email = user_data.get('email')
        self.colleagues = self.get_colleagues(self.__server)

