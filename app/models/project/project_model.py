

class ProjectModel:
    def __init__(self, _id, name, owner_id, root, fps, status):
        self.id = _id
        self.name = name
        self.owner_id = owner_id
        self.root = root
        self.fps = fps
        self.status = status

    @staticmethod
    def get_user_projects(server, user_id):
        respone = server.get_user_projects(user_id)
        if not respone[0]:
            return []

        projects = []
        for prj in respone[1]:
            project = ProjectModel(prj["project_id"],
                                   prj["name"],
                                   prj["owner_id"],
                                   prj["path"],
                                   prj["fps"],
                                   prj["status"])
            projects.append(project)
        return projects
