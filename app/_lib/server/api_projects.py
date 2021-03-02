
class ApiProjects:
    def create_project(self, project_name, owner_id, root_id,
                       scheme, fps, status):
        method_name = "create_project"
        args = [f"{project_name}",
                f"{owner_id}",
                f"{root_id}",
                f"{scheme}",
                f"{fps}",
                f"{status}"]

        response = self.send_request(method_name, args)
        return response

    def get_user_projects(self, user_id):
        method_name = "get_user_projects"
        args = [f"{user_id}"]

        response = self.send_request(method_name, args)
        return response

