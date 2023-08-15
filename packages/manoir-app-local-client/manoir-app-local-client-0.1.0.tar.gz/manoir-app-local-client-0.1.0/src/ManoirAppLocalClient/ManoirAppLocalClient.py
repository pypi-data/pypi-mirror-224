import requests
import json

class ManoirAppLocalClient:
    """Class to make authenticated requests."""

    def __init__(self, host: str, user: str, password:str):
        """Initialize the auth."""
        self.host = host
        self.session = requests.Session()
        self.session.auth = (user, password)

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        """Make a request."""
        return self.session.request(
            method, f"{self.host}/{path}", verify=False, **kwargs
        )
    
    def invokeScene(self, scenegroup:str, sceneId:str):

        body = {
            "SceneId":sceneId
        }
        response = self.request("POST", f"v1.0/agents/all/send/homeautomation.scenario.execute", json= body).json()
        