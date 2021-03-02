class RootModel:
    def __init__(self, _id, owner_id, root_folder, sharing):
        self.id = _id
        self.owner_id = owner_id
        self.root_folder = root_folder
        self.sharing = sharing

    @staticmethod
    def get_user_roots(server, user_id):
        respone = server.get_user_roots(user_id)
        if not respone[0]:
            return []

        roots = []
        for root_data in respone[1]:
            root = RootModel(root_data["root_id"],
                             f"{user_id}",
                             root_data["root_folder"],
                             root_data["sharing"])
            roots.append(root)
        return roots



