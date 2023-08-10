from .Client import Client
from .Image import Image


def set_access_token(access_token=""):
    if len(access_token) == 0:
        raise Exception("\n\nNo access token was provided. Please pass a token to the set_access_token"
                        " function or set the token in the __token__.py file. Check the README for more"
                        " information.\n")

    Client.init_static(access_token)
