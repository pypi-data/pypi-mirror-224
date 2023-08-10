import requests


class Client:
    session = None
    access_token = None
    initialised = False

    @staticmethod
    def init_static(access_token: str):
        Client.access_token = access_token
        Client.session = requests.Session()
        Client.session.headers.update({"Authorization": f"OAuth {Client.access_token}"})
        Client.initialised = True

    @staticmethod
    def get(url: str, params: dict = None):

        if not Client.initialised:
            raise Exception("\n\nNo access token was provided. Please pass a token to the set_access_token"
                            " function or set the token in the __token__.py file. Check the README for more"
                            " information.\n")

        request = requests.Request('GET', url, params=params)
        prepared_request = Client.session.prepare_request(request)
        response = Client.session.send(prepared_request)
        response.raise_for_status()
        return response.json()
