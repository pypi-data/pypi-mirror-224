import requests


class Client:
    session = None
    access_token = None

    @staticmethod
    def init_static(access_token: str):
        Client.access_token = access_token
        Client.session = requests.Session()
        Client.session.headers.update({"Authorization": f"OAuth {Client.access_token}"})

    @staticmethod
    def get(url: str, params: dict = None):
        request = requests.Request('GET', url, params=params)
        prepared_request = Client.session.prepare_request(request)
        response = Client.session.send(prepared_request)
        response.raise_for_status()
        return response.json()
