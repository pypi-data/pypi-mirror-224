import requests
import urllib.parse

from decouple import config

class GitlabClient:
    
    def __init__(self, api_token: str, *args, **kwargs):
        self.api_token = api_token
        self.api_url = "https://gitlab.com/api/v4"
        self.headers = {"PRIVATE-TOKEN": self.api_token}
        super(GitlabClient, self).__init__(*args, **kwargs)

    def clean_url(self, route: str):
        return f'{self.api_url}/{route}?owned=yes'
    
    def encode_path(self, path):
        return urllib.parse.quote(path, safe='')
    
    def generate_response(self, method: str, route: str, **kwargs):
        match method:
            case "POST":
                response = requests.post(self.clean_url(route), headers=self.headers, data=kwargs)
            case "GET":
                response = requests.get(self.clean_url(route),  headers=self.headers)
            case _:
                response = None
        return response
        
    def groups(self):
        response = self.generate_response("GET", "groups")
        return response.json()
    
    def projects(self):
        response = self.generate_response("GET", "projects")
        return response.json()
    
    def project(self, project_full_path):
        response = self.generate_response("GET", f"projects/{self.encode_path(project_full_path)}")
        return response.json()
    
if __name__ == '__main__':
    client = GitlabClient(config('GITLAB_API_TOKEN'))
    print(client.__dict__)