from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        # client = Client('http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl')
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        # client = Client('http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl')
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            project_list = client.service.mc_projects_get_user_accessible(username, password)
            result_list = []
            for project in project_list:
                result_list.append(Project(id=project.id, name=project.name))
            return result_list
        except WebFault:
            return None