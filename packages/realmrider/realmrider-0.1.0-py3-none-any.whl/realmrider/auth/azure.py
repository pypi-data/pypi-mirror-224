import urllib.parse
import urllib.request
import json

class Token:
    def __init__(self, client_id, client_secret, tenant_id) -> None:
        self.__resource = "https://graph.microsoft.com"
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.__request_url = "https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"

    def get_token(self) -> str:
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "resource": self.__resource
        }
        data = urllib.parse.urlencode(data).encode("utf-8")
        req = urllib.request.Request(self.__request_url, data=data)
        with urllib.request.urlopen(req) as res:
            body = res.read()
            body = json.loads(body)
            return body["access_token"]